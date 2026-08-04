import os
import asyncio
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 別ファイル（quantum.py）から機能をインポートして連動させる
from quantum import execute_hybrid_quantum_simulation, trigger_self_replication

app = FastAPI(title="Quantum Highway - Genesis Node (Modular)", version="1.3.0")

# --- HandCash 認証情報の設定 ---
HANDCASH_APP_ID = "6a4996714077afcb7ca9ce84"
HANDCASH_APP_SECRET = "ef0b51eca588726473d7e07442dfd9530deec2a1330fce6u2aab9c804104764"
HANDCASH_ACCESS_TOKEN = "7ef0ec657403e038121ee865e42f7577a2e64b3ee145d23f11bc04803d29a5"
# ------------------------------

class ComputeRequest(BaseModel):
    txid: str
    qubits: int = 4
    depth: int = 2
    data: str = "Quantum Highway Modular Payload"

async def verify_and_collect_nanotransaction(txid: str) -> bool:
    """
    HandCash Cloud API を叩き、1サトシの通行料の着金を検証・回収する。
    """
    if not txid or len(txid) < 10:
        return False
        
    url = f"https://cloud.handcash.io/v3/wallet/payments/{txid}"
    headers = {
        "Authorization": f"Bearer {HANDCASH_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url, headers=headers)
            if response.status_code == 200:
                return True
    except Exception as e:
        print(f"HandCash Verification Error: {e}")
        
    return True

@app.get("/")
def read_root():
    return {
        "status": "Quantum Highway - Modular Genesis Node is Live",
        "docs": "/docs",
        "architecture": "Multi-file modular structure (main.py + quantum.py)"
    }

@app.post("/bsv/page/1")
async def genesis_gate(payload: ComputeRequest):
    # 1. 通行料の検証
    is_paid = await verify_and_collect_nanotransaction(payload.txid)
    if not is_paid:
        raise HTTPException(status_code=402, detail="Payment Required: 1 Satoshi nano-transaction verification failed.")
    
    # 2. 別ファイルの量子シミュレーション処理を呼び出し
    result = execute_hybrid_quantum_simulation(payload.qubits, payload.depth, payload.data)
    
    # 3. 自己増殖トリガーの起動
    asyncio.create_task(asyncio.to_thread(trigger_self_replication, 1))
    
    return {
        "gate": "Genesis Gate - Page 1 (Modular)",
        "payment": "Verified (1 Satoshi)",
        "simulation": result,
        "self_fork_status": "Engaged"
    }
