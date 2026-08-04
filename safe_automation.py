import asyncio
import logging
import random
from typing import Dict, Any

# ログ設定（安全な運用監視のため詳細に出力）
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(levelname)s] %(message)s")
logger = logging.getLogger("SafeAutomation")

class SafeAutomationEngine:
    def __init__(self, max_nodes: int = 128, interval_sec: float = 3.0):
        self.max_nodes = max_nodes
        self.interval_sec = interval_sec  # スパム化を防ぐため適切なインターバルを設定
        self.current_nodes = 16
        self.is_active = False
        self.treasury_pool = 1000000  # 安全な初期プール

    async def safe_execute_task(self) -> Dict[str, Any]:
        """レートリミットと安全装置を考慮した単一タスクの実行"""
        try:
            # 安全な範囲でのみノード数を拡張（上限を厳格にガード）
            if self.current_nodes < self.max_nodes and random.random() > 0.6:
                self.current_nodes += 4
                
            # 報酬の安全な加算シミュレーション
            earned = 50000 * (self.current_nodes // 8)
            self.treasury_pool += earned

            logger.info(f"タスク正常完了: アクティブノード={self.current_nodes}, 獲得報酬={earned}サトシ")
            
            return {
                "status": "SUCCESS",
                "active_nodes": self.current_nodes,
                "earned_sats": earned,
                "total_treasury": self.treasury_pool
            }
        except Exception as e:
            logger.error(f"予期せぬエラーを検出し安全に保護しました: {e}")
            return {"status": "ERROR", "message": str(e)}

    async def run_safe_loop(self):
        """スパム化・暴走を防ぐウェイトを挟んだ永久稼働ループ"""
        self.is_active = True
        logger.info("安全設計オートメーション・エンジンが起動しました。")
        
        while self.is_active:
            # 1. タスクの安全実行
            await self.safe_execute_task()
            
            # 2. 暴走・過負荷を防ぐためのインターバル（スリープ）
            await asyncio.sleep(self.interval_sec)

    def stop(self):
        self.is_active = False
        logger.info("安全エンジンの稼働を停止しました。")

# 単体テスト用のエントリポイント
if __name__ == "__main__":
    engine = SafeAutomationEngine(max_nodes=64, interval_sec=2.0)
    try:
        asyncio.run(engine.run_safe_loop())
    except KeyboardInterrupt:
        engine.stop()
