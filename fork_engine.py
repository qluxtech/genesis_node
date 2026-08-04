import time

class NodeRegistry:
    def __init__(self):
        # 稼働中のサブノードや蓄積されたエネルギー（サトシ換算）を管理
        self.active_nodes = [1]
        self.total_earned_sats = 0

    def register_fork(self, parent_id: int) -> int:
        next_id = parent_id * 10 + 1
        if next_id not in self.active_nodes:
            self.active_nodes.append(next_id)
        return next_id

    def add_sats(self, amount: int = 1):
        self.total_earned_sats += amount
        return self.total_earned_sats

# グローバルなノード管理インスタンス
registry = NodeRegistry()

def generate_fork_payload(parent_id: int, complexity: int):
    """
    負荷や複雑度に応じて新しいサブノードの枠組みを動的に生成する
    """
    if complexity > 50:
        new_node_id = registry.register_fork(parent_id)
        current_sats = registry.add_sats(1)
        return {
            "fork_status": "Spawned",
            "spawned_node": f"/bsv/page/{new_node_id}",
            "accumulated_sats": current_sats,
            "timestamp": time.time()
        }
    return {
            "fork_status": "Stable",
            "accumulated_sats": registry.total_earned_sats,
            "timestamp": time.time()
    }
