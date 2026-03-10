import asyncio
import torch
import numpy as np
from pydantic import BaseModel, ValidationError
from typing import List

# --- DAY 3: THE CONTRACT ---
class LogEntry(BaseModel):
    id: int
    msg: str
    severity: float # Should be 0.0 to 1.0

# --- DAY 2: THE DATA STREAM ---
def log_stream():
    logs = [
        {"id": 1, "msg": "CPU Normal", "severity": 0.1},
        {"id": 2, "msg": "NIL POINTER", "severity": "CRITICAL"}, # BUG HERE?
        {"id": 3, "msg": "DB Timeout", "severity": 0.9}
    ]
    for log in logs:
        yield log

# --- DAY 4: THE ASYNC PROCESSOR ---
async def analyze_log(log_obj):
    print(f"Analyzing: {log_obj.msg}...")
    await asyncio.sleep(0.5)
    # --- DAY 6: THE NEURAL CHECK ---
    # We expect a 1x1 tensor, but we are doing a shape mismatch
    weights = torch.tensor([0.5, 0.5]) 
    input_val = torch.tensor([log_obj.severity])
    risk = torch.matmul(weights, input_val) # BUG HERE: Shape Mismatch
    return risk.item()

# --- DAY 1: THE SCOPING BUG ---
processed_count = 0

async def main():
    stream = log_stream()
    
    # BUG: Generator Exhaustion - If we loop twice, what happens?
    print(f"Total logs in stream: {len(list(stream))}") 
    
    for raw_log in stream:
        try:
            # Validate
            log_obj = LogEntry(**raw_log)
            
            # BUG: Missing Await
            risk_score = analyze_log(log_obj) 
            
            if risk_score > 0.5:
                # BUG: Scoping/Global Issue
                processed_count += 1
                print(f"⚠️ High Risk Detected! Total: {processed_count}")
                
        except ValidationError as e:
            print(f"❌ Validation Failed: {e.json()}")

if __name__ == "__main__":
    asyncio.run(main())