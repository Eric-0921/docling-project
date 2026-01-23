import time
import psutil
import yaml
import os
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.live import Live
from rich.table import Table
from rich.panel import Panel

class TaskMonitor:
    def __init__(self, total_chunks, pricing_config_path="ai_adapter/translation_agent/config/pricing.yaml"):
        self.console = Console()
        self.total_chunks = total_chunks
        self.pricing = self._load_pricing(pricing_config_path)
        
        # Metrics
        self.processed_chunks = 0
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.cache_hit_tokens = 0
        self.cache_miss_tokens = 0
        self.total_cost = 0.0
        self.start_time = time.time()
        
        # Hardware Baseline
        self.gpu_available = self._check_gpu()

    def _load_pricing(self, path):
        try:
            with open(path, 'r') as f:
                return yaml.safe_load(f)
        except:
            return {"models": {"deepseek-chat": {"input_cache_hit": 0.14, "input_cache_miss": 0.28, "output": 1.10}}}

    def _check_gpu(self):
        return os.system("which nvidia-smi > /dev/null") == 0

    def update_metrics(self, usage, model="deepseek-chat"):
        """
        Update metrics based on API response usage dictionary.
        usage: {'prompt_tokens': 100, 'completion_tokens': 50, 'prompt_cache_hit_tokens': 80, ...}
        """
        self.processed_chunks += 1
        
        # Parse usage
        p_tokens = usage.get('prompt_tokens', 0)
        c_tokens = usage.get('completion_tokens', 0)
        
        # DeepSeek specific fields
        hit_tokens = usage.get('prompt_cache_hit_tokens', 0)
        miss_tokens = usage.get('prompt_cache_miss_tokens', p_tokens - hit_tokens)
        
        self.total_input_tokens += p_tokens
        self.total_output_tokens += c_tokens
        self.cache_hit_tokens += hit_tokens
        self.cache_miss_tokens += miss_tokens
        
        # Calculate Cost
        prices = self.pricing['models'].get(model, self.pricing['models']['deepseek-chat'])
        cost_input = (hit_tokens / 1e6 * prices['input_cache_hit']) + (miss_tokens / 1e6 * prices['input_cache_miss'])
        cost_output = (c_tokens / 1e6 * prices['output'])
        self.total_cost += (cost_input + cost_output)

    def get_hardware_stats(self):
        cpu_pct = psutil.cpu_percent()
        ram_pct = psutil.virtual_memory().percent
        gpu_stat = "N/A"
        
        if self.gpu_available:
            # Simple check via nvidia-smi query
            try:
                # This is expensive to call every time, maybe optimize later
                # For now just return a placeholder or simple check
                pass
            except:
                pass
        return f"CPU: {cpu_pct}% | RAM: {ram_pct}%"

    def display(self):
        """
        Returns a renderable for Rich Live display.
        """
        # Create Layout
        elapsed = time.time() - self.start_time
        speed = self.processed_chunks / elapsed if elapsed > 0 else 0
        eta = (self.total_chunks - self.processed_chunks) / speed if speed > 0 else 0
        
        metrics_table = Table(show_header=False, box=None)
        metrics_table.add_row("💰 Total Cost", f"${self.total_cost:.4f}")
        metrics_table.add_row("🧠 Cache Hit Rate", f"{self.cache_hit_tokens / (self.total_input_tokens+1) * 100:.1f}%")
        metrics_table.add_row("⚡ Speed", f"{speed:.2f} chunks/s")
        metrics_table.add_row("⏱️ ETA", f"{eta/60:.1f} min")
        
        hw_panel = Panel(self.get_hardware_stats(), title="Hardware", border_style="blue")
        metrics_panel = Panel(metrics_table, title="Metrics", border_style="green")
        
        return metrics_panel
