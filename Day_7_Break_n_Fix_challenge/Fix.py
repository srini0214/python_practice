import asyncio
import torch
from pydantic import BaseModel, ValidationError, field_validator
from typing import Union

# --- FIX 3: THE CONTRACT (Handling "CRITICAL" string) ---
class LogEntry(BaseModel):
    id: int
    msg: str
    severity: float 

    @field_validator('severity', mode='before')
    @classmethod
    def handle_critical_string(cls, v: Union[float, str]) -> float:
        if isinstance(v, str) and v.upper() == "CRITICAL":
            return 1.0  # Map domain logic to float
        return float(v)

# --- FIX 2: THE DATA STREAM (Preventing Exhaustion) ---
def log_stream():
    logs = [
        {"id": 1, "msg": "CPU Normal", "severity": 0.1},
        {"id": 2, "msg": "NIL POINTER", "severity": "CRITICAL"}, 
        {"id": 3, "msg": "DB Timeout", "severity": 0.9}
    ]
    for log in logs:
        yield log

# --- FIX 4 & 5: ASYNC & TENSORS ---
async def analyze_log(log_obj: LogEntry):
    print(f"Analyzing: {log_obj.msg}...")
    await asyncio.sleep(0.5) 
    
    # FIX 5: Shape Alignment (Dot product of 1x1 vectors)
    weight = torch.tensor([0.9]) # High importance weight
    input_val = torch.tensor([log_obj.severity])
    
    # dot product / matmul requires matching dimensions
    risk = torch.matmul(weight, input_val) 
    return risk.item()

# --- FIX 1: SCOPING (State Management) ---
async def main():
    # Fix 2: Don't call list(stream) before looping!
    stream = log_stream()
    processed_count = 0 
    
    for raw_log in stream:
        try:
            log_obj = LogEntry(**raw_log)
            
            # FIX 4: Properly await the coroutine
            risk_score = await analyze_log(log_obj) 
            
            if risk_score > 0.5:
                # FIX 1: Variable is now in the local scope of main()
                processed_count += 1
                print(f"⚠️ High Risk Detected! Total: {processed_count}")
                
        except ValidationError as e:
            # Day 5: Structured error inspection
            print(f"❌ Validation Failed for ID {raw_log.get('id')}: {e.errors()[0]['msg']}")

if __name__ == "__main__":
    asyncio.run(main())