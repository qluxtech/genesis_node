import os
import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
try:
    import qulacs
except ImportError:
    qulacs = None

app = FastAPI(title="Quantum Highway - Genesis Node", version="1.0.0")

@app.get("/")
def read_root():
    return {"status": "Quantum Highway - Genesis Node is Live", "docs": "/docs"}

class ComputeRequest(BaseModel):
    txid: str
    qubits: int = 4
    depth: int = 2

@app.post("/bsv/page/1")
async def genesis_gate(payload: ComputeRequest):
    return {"status": "success", "qubits": payload.qubits}
