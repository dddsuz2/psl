import asyncio
import random

async def random_stream(max_val):
    while True:
        yield random.randint(1, max_val)
        await asyncio.sleep(0.1)

async def main():
    async_iter = aiter(random_stream(100))
    
    try:
        for _ in range(10):
            val = await async_iter.__anext__()
            print(val)
    finally:
        await async_iter.aclose()

if __name__ == "__main__":
    asyncio.run(main())
