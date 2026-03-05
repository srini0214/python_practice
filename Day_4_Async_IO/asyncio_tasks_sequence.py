import asyncio
import time


async def fetch_data(param):
    print(f"Do something with {param}...")
    # this awaits the background task to be completed
    # This is true async here , since the eventloop suspends the
    # current thread (until the background sleep/task is complete)
    # meanwhile it can go and attned the next avaialble task in queue
    # i.e 'task2' execution
    await asyncio.sleep(param) 
    print(f"Done with {param}")
    return f"Result of {param}"


async def main():
    # create_task just creates and schedules an coroutine task to run on event loop and returns the task obj
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    # the below await task2 actually yields the control to the 
    # eventloop and suspend the main() coroutine
    # until the task2 is complete
    result2 = await task2
    print("Task 2 fully completed")
    # the below 'await task1' actually yields the control to the 
    # eventloop and suspend the main() coroutine until the task1 is complete
    result1 = await task1
    print("Task 1 fully completed")
    return [result1, result2]

### please note, we are awaiting task2 and then task1, but still the 
# eventloop will execute the task1 first , since it is in the FIFO queue
# for eventloop to pick it first for execution.

t1 = time.perf_counter()

results = asyncio.run(main()) # main coroutine starts running on eventloop
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f} seconds")