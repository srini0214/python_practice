import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    return {"data": "success"}

def main():
    # ERROR: You cannot just call an async function like this!
    result = fetch_data() 
    print(result["data"])

main()