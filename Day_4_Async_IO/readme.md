Best Async IO tutorial - https://github.com/CoreyMSchafer/AsyncIO-Code-Examples


we tackle the biggest performance killer in AI systems: Latency. As a Senior Architect, you know that "speed" in a distributed system usually isn't about how fast the CPU calculates; it's about how efficiently you wait. In an AI Agentic workflow, your code spends 95% of its time waiting for a Model to generate tokens or a Vector DB to return chunks.

If you do this synchronously, your system is "Blocking." If you do it with AsyncIO, your system is "Non-blocking."

1. The "Waiter" Metaphor
Imagine a restaurant (your Python script):

Synchronous: The waiter takes an order, walks to the kitchen, and stands there until the food is ready before serving the next table. (Total time: 10 mins per table).

AsyncIO: The waiter takes an order, gives it to the kitchen, and immediately goes to the next table while the food cooks. (Total time: 2 mins per table).

In AI terms: While the LLM is "cooking" your response, your Python script can be fetching the next set of documents from the database.

2. The Core Vocabulary
You only need to master four keywords to think in Async:

async def: Defines a Coroutine. Calling this function doesn't run it; it just creates a "task" object.

await: Tells Python: "You can pause me here and go do other work until this specific task is finished."

asyncio.run(): The entry point that starts the Event Loop.

asyncio.gather(): The "Parallelizer." It kicks off multiple tasks at once and waits for all of them to report back.

Exercise 1: The "Fire and Forget" vs. "Wait"

Task: Modify the main() function above. Instead of using gather, call each agent one by one using await:

Python
res1 = await call_llm("Agent 1", 2)
res2 = await call_llm("Agent 2", 2)
Question: What is the total time now? Why would an architect ever choose this "slower" way? (Hint: Think about dependencies—does Agent 2 need Agent 1's output?)

Exercise 2: The Timeout Guardrail

In a Bank or Insurance company, you can't have a UI hanging forever because a model is slow.

Task: Use asyncio.wait_for(task, timeout=2.0) to wrap an LLM call.

Challenge: Write a try/except block that catches asyncio.TimeoutError and returns a "Cached/Default" response if the AI takes too long.

Exercise 3: The Async File Reader

AI Pipelines often read many small text files (RAG docs).

Task: Research the aiofiles library. Why is standard open().read() bad inside an async def function?

Day 4 Check-point: The "Event Loop" Trap

A common senior-level mistake is putting a "CPU-heavy" task (like calculating a massive matrix or a long for x in range(10**9)) inside an async function.

Warning: AsyncIO is for I/O (waiting for networks/disks). If you do heavy math in an async function, you "block the loop," and all your other "waiters" freeze. For math, we use Multi-processing.