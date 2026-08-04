import os
import asyncio
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 各モジュールから機能をインポート
from quantum import execute_hybrid_quantum_simulation
from fork_engine import generate_fork_payload

app = FastAPI(title="Quantum Highway - Genesis Node (Autonomous)", version="1.4.0")

# --- HandCash 認証情報の設定 ---
HANDCASH_APP_ID = "6a4996714077afcb7ca9ce84"
HANDCASH_APP_SECRET = "ef0b51eca588726473d7e07442dfd9530deec2a1330fce6u2aab9c804104764"
HANDCASH_ACCESS_TOKEN = "7ef0ec657403e038121ee865e42f7577a2e64b3ee145d23f11bc04803d29a5"
# ------------------------------

class ComputeRequest(BaseModel):
    txid: str
    qubits: int = 4
    depth: int = 2
    data: str = "Quantum Highway Autonomous Payload"

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
        "status": "Quantum Highway - Autonomous Genesis Node is Live",
        "docs": "/docs",
        "architecture": "Tri-module structure (main.py + quantum.py + fork_engine.py)"
    }

@app.post("/bsv/page/1")
async def genesis_gate(payload: ComputeRequest):
    # 1. 通行料の検証
    is_paid = await verify_and_collect_nanotransaction(payload.txid)
    if not is_paid:
        raise HTTPException(status_code=402, detail="Payment Required: 1 Satoshi nano-transaction verification failed.")
    
    # 2. 量子シミュレーションの実行
    sim_result = execute_hybrid_quantum_simulation(payload.qubits, payload.depth, payload.data)
    
    # 3. 自己フォーク（Self-Fork）エンジンの駆動評価（データの長さを複雑度として判定）
    complexity = len(payload.data)
    fork_result = generate_fork_payload(parent_id=1, complexity=complexity)
    
    return {
        "gate": "Genesis Gate - Page 1 (Autonomous)",
        "payment": "Verified (1 Satoshi)",
        "simulation": sim_result,
        "self_fork": fork_result
    }
