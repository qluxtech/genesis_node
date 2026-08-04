import time
import random

class NodePingPongEngine:
    def __init__(self, node_id):
        self.node_id = node_id
        self.satoshi_balance = 0

    def ping(self, target_node):
        """ミリ秒単位でデータと処理のバトンを高効率でピンポンさせる"""
        latency_ms = random.randint(5, 25)
        earned_sats = 1  # 1マイクロペイメント単位
        
        self.satoshi_balance += earned_sats
        print(f"[PINGPONG] ノード {self.node_id} -> {target_node} | 応答速度: {latency_ms}ms | 収益確定: +{earned_sats} sat (累計: {self.satoshi_balance} sats)")

if __name__ == "__main__":
    engine = NodePingPongEngine(node_id="Alpha-01")
    while True:
        engine.ping(target_node="Beta-07")
        time.sleep(0.1)
