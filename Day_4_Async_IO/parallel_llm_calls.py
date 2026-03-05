import asyncio
import time

async def call_llm(agent_name, delay):
    print(f"[{agent_name}] Starting analysis...")
    await asyncio.sleep(delay) # Simulating an LLM API call
    return f"[{agent_name}] Analysis Complete"

async def main():
    start_time = time.time()
    
    # Kicking off 3 'agents' at the exact same time
    """ results = await asyncio.gather(
        call_llm("Security-Agent", 3),
        call_llm("Performance-Agent", 2),
        call_llm("Logic-Agent", 4)
    )"""

    res1 = await call_llm("Agent 1", 2)
    res2 = await call_llm("Agent 2", 2)
    
    """for r in results:
        print(r)"""
        
    print(f"Total time taken: {time.time() - start_time:.2f} seconds")

# Run the event loop
asyncio.run(main())