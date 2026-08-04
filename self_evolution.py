import time
from typing import Dict, Any

class SelfEvolutionEngine:
    def __init__(self):
        self.config = {
            "processing_weight": 1.0,
            "pulse_threshold_ms": 100.0,
            "concurrency_limit": 50,
            "generation": 1
        }
        self.history = []

    def evaluate_and_adapt(self, avg_latency_ms: float, error_rate: float) -> Dict[str, Any]:
        """負荷・レイテンシに基づくパラメータの動的最適化"""
        old_config = self.config.copy()
        
        # レイテンシ高負荷時の自動スロットル調整
        if avg_latency_ms > 150.0:
            self.config["pulse_threshold_ms"] += 10.0
            self.config["concurrency_limit"] = max(10, self.config["concurrency_limit"] - 5)
        elif avg_latency_ms < 50.0 and error_rate == 0.0:
            self.config["processing_weight"] = round(self.config["processing_weight"] * 1.05, 3)
            self.config["concurrency_limit"] += 5

        self.config["generation"] += 1
        
        adaptation_log = {
            "generation": self.config["generation"],
            "previous": old_config,
            "current": self.config,
            "adapted_at": time.time()
        }
        self.history.append(adaptation_log)
        
        print(f"[EVOLUTION] 世代 #{self.config['generation']} 昇格 | 並列上限: {self.config['concurrency_limit']} | 処理重み: {self.config['processing_weight']}")
        return self.config

if __name__ == "__main__":
    evo = SelfEvolutionEngine()
    evo.evaluate_and_adapt(avg_latency_ms=35.2, error_rate=0.0)
    evo.evaluate_and_adapt(avg_latency_ms=180.5, error_rate=0.02)
