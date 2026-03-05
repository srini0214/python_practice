import asyncio
import time


# suync function
def sync_function(test_param: str) -> str:
    print("This is an synchronous function")
    time.sleep(0.1)
    return f"Sync result: {test_param}"

# coroutine function
async def async_function(test_param: str) -> str:
    print("This is an asynchronous coroutine function")
    await asyncio.sleep(0.1)
    return f"Async result: {test_param}"


async def main():
    coroutine_obj = async_function("Test")
    print(f"coroutine_obj: {coroutine_obj}")

    coroutine_result = await coroutine_obj
    print(coroutine_result)

if __name__ == "__main__":
    asyncio.run(main())