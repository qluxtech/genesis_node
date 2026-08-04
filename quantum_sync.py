import asyncio
import random
import time
from typing import Dict, Any

class QuantumSyncLoop:
    def __init__(self, node_id: str = "Genesis-Core-01"):
        self.node_id = node_id
        self.phase_angle = 0.0
        self.entropy = 0.01
        self.is_running = False

    async def synchronize_phase(self) -> Dict[str, Any]:
        """量子状態パラメータの動的更新"""
        self.phase_angle = (self.phase_angle + random.uniform(0.1, 0.5)) % 360.0
        self.entropy = round(random.uniform(0.001, 0.05), 4)
        
        state_data = {
            "node_id": self.node_id,
            "timestamp": time.time(),
            "phase_angle_deg": round(self.phase_angle, 2),
            "entropy_index": self.entropy,
            "sync_status": "LOCKED" if self.entropy < 0.04 else "CALIBRATING"
        }
        return state_data

    async def start_loop(self, interval_sec: float = 1.0):
        """バックグラウンド同期ループの開始"""
        self.is_running = True
        print(f"[QUANTUM_SYNC] ノード [{self.node_id}] 動的位相同期ループ起動...")
        
        while self.is_running:
            state = await self.synchronize_phase()
            print(f"[QUANTUM_SYNC] 位相: {state['phase_angle_deg']}° | エントロピー: {state['entropy_index']} | ステータス: {state['sync_status']}")
            await asyncio.sleep(interval_sec)

if __name__ == "__main__":
    sync_engine = QuantumSyncLoop()
    asyncio.run(sync_engine.start_loop(0.5))
