1. The Architectural Choice: Eager vs. Lazy
In your 15-year career, you've seen this in databases: Eager (Load the whole table) vs. Lazy (Cursor/Stream).

Comprehensions (Eager): Python builds the entire object in RAM immediately.

Generators (Lazy): Python builds a "promise" to compute the next value only when requested.

The Memory Benchmark

If you need to process 1,000,000 log lines:

List Comprehension: Uses ~80MB of RAM immediately.

Generator Expression: Uses ~120 bytes regardless of the dataset size.

2. Comprehensions: The Data Transformation Glue
Comprehensions are the "Pythonic" way to replace map() and filter(). In AI, we use these to prep JSON for model input.

List, Dict, and Set

Type	Syntax	Best Use Case
List	[x for x in data]	Finalizing a batch for a GPU.
Dict	{k: v for k, v in data}	Mapping token_id to token_string.
Set	{x for x in data}	Deduplicating a list of document IDs for RAG.
The Architect's Code:

Python
# Mapping raw database results to a clean model input
raw_users = [{"id": 1, "role": "admin"}, {"id": 2, "role": "user"}]

# Pythonic Dict Comprehension
user_map = {u["id"]: u["role"] for u in raw_users if u["role"] == "admin"}
3. Generators: The Heart of AI Streaming
When you use ChatGPT and the text "types out," you are consuming a Generator. In PyTorch, when you load a 50GB dataset, the DataLoader is a Generator.

The yield Keyword

Unlike return, yield pauses the function and saves its state.

Python
def stream_tokens(text):
    for word in text.split():
        # Think of this as 'pausing' the function and handing a word to the UI
        yield word 

# The consumer controls the speed
token_gen = stream_tokens("The model is thinking...")
print(next(token_gen)) # "The"
# ... 5 minutes later ...
print(next(token_gen)) # "model"
Day 2 Exercises
Exercise 1: The RAG Filter (List Comprehension)

You have a list of search results from a vector database. Each result is a dict: {"doc_id": int, "score": float, "content": str}.

Task: Write a single-line list comprehension to get only the doc_id of results where the score > 0.85.

Input: results = [{"doc_id": 1, "score": 0.9}, {"doc_id": 2, "score": 0.7}]

Exercise 2: The "Infinite" SRE Log Stream (Generator)

Goal: Simulate a system that monitors a log file that never ends.

Task: Write a generator function follow_logs(file_obj) that uses a while True loop to check for new lines and yield them.

Architect Question: Why is a Generator better than file.readlines() for a production SRE tool?

Exercise 3: Memory Profiling (The "OOM" Test)

Task: Run the following two lines in your terminal (using sys.getsizeof).

Python
import sys
# A: List of squares
a = [x**2 for x in range(1000000)]
# B: Generator of squares
b = (x**2 for x in range(1000000))

print(f"List Size: {sys.getsizeof(a)} bytes")
print(f"Gen Size: {sys.getsizeof(b)} bytes")
Observation: Note that the Generator size stays the same even if you change 1000000 to 1000000000.

Day 2 "Architect's Insight"

Generators are one-time use. Once you iterate through a generator (using a for-loop or list(gen)), it is exhausted. If you need the data again, you must recreate the generator. This is a common bug when debugging RAG pipelines!