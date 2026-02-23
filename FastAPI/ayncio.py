import asyncio
import time

async def main():
    for i in range(1,6):
        print("main", i)
        await myfunction(i)

async def myfunction(i):
    print("my function", i)
    time.sleep(2)

asyncio.run(main())
