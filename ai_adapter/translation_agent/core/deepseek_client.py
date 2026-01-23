import os
import json
import yaml
import time
import random
from openai import OpenAI
from .cache_manager import CacheManager

# 网络重试配置
MAX_RETRIES = 5
BASE_DELAY = 2  # 秒
MAX_DELAY = 60  # 最大延迟

class DeepSeekClient:
    def __init__(self, api_key_path="api_keys.yml", settings_path="ai_adapter/translation_agent/config/settings.yaml"):
        self.api_key = self._load_api_key(api_key_path)
        self.settings = self._load_settings(settings_path)
        self.client = OpenAI(api_key=self.api_key, base_url=self.settings['base_url'])
        self.cache_manager = CacheManager()
        self.system_prompt = self.cache_manager.get_system_prompt()
        
    def _load_api_key(self, path):
        try:
            with open(path, 'r') as f:
                for line in f:
                    if 'deepseek_api_key' in line:
                        return line.split(':', 1)[1].strip()
        except:
            pass
        return os.environ.get("DEEPSEEK_API_KEY")

    def _load_settings(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def translate(self, text):
        """
        发送文本至 DeepSeek 并返回翻译结果。
        包含指数退避重试机制以应对网络波动。
        """
        last_exception = None
        
        for attempt in range(MAX_RETRIES):
            try:
                messages = [
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": text}
                ]
                
                response = self.client.chat.completions.create(
                    model=self.settings['model'],
                    messages=messages,
                    temperature=self.settings['temperature'],
                    stream=False,
                    response_format=self.settings.get('response_format', {"type": "json_object"})
                )
                
                content = response.choices[0].message.content
                usage = response.usage.model_dump() if response.usage else {}

                # 解析 JSON
                try:
                    data = json.loads(content)
                    if "translation" in data:
                        return data["translation"], usage
                    else:
                        return str(data), usage
                except json.JSONDecodeError:
                    print(f"Warning: 模型返回了无效 JSON。原始内容: {content[:100]}...")
                    return text, usage  # 安全回退

            except Exception as e:
                last_exception = e
                
                # 判断是否为可重试的网络错误
                error_str = str(e).lower()
                is_retryable = any(keyword in error_str for keyword in [
                    'timeout', 'connection', 'network', 'ssl', 'eof', 
                    'reset', 'refused', 'unavailable', '502', '503', '504'
                ])
                
                if is_retryable and attempt < MAX_RETRIES - 1:
                    # 指数退避 + 随机抖动
                    delay = min(BASE_DELAY * (2 ** attempt) + random.uniform(0, 1), MAX_DELAY)
                    print(f"[Retry {attempt + 1}/{MAX_RETRIES}] 网络错误: {e}. 等待 {delay:.1f}s 后重试...")
                    time.sleep(delay)
                else:
                    # 不可重试的错误或已达最大重试次数
                    print(f"API Error (不可恢复): {e}")
                    break
        
        # 所有重试均失败
        print(f"[FAILED] 在 {MAX_RETRIES} 次尝试后仍然失败。返回原始文本。")
        return text, {}

