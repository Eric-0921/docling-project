import yaml
import os

class CacheManager:
    def __init__(self, config_dir="ai_adapter/translation_agent/config"):
        self.config_dir = config_dir
        self.glossary = self._load_glossary()
        self.prompt_template = self._load_template()

    def _load_glossary(self):
        try:
            with open(os.path.join(self.config_dir, "glossary.yaml"), "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                terms = data.get("terms", {})
                # Format as string for prompt
                return '\n'.join([f"- {k}: {v}" for k, v in terms.items()])
        except Exception:
            return ""

    def _load_template(self):
        try:
            with open(os.path.join(self.config_dir, "prompt_template.md"), "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            return "Translate the following to Chinese:\n{glossary_content}"

    def get_system_prompt(self):
        """
        Returns the fully constructed system prompt.
        This prompt should be static across requests to hit KV Cache.
        """
        return self.prompt_template.replace("{glossary_content}", self.glossary)
