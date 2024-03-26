import asyncio
import aiohttp

async def fetch_data(session, url):
    async with session.get(url) as response:
        data = await response.text()
        return data
    
async def main():
    urls = [
        "https://my-json-server.typicode.com/typicode/demo/posts",
        "https://my-json-server.typicode.com/typicode/demo/comments",
        "https://my-json-server.typicode.com/typicode/demo/profile",
        "https://my-json-server.typicode.com/typicode/demo/db"
    ]

    async with aiohttp.ClientSession() as session:
        data_iterator = aiter(await fetch_data(session, url) for url in urls)
        
        try:
            while True:
                data = await anext(data_iterator)
                print(f'Received Data: {data}')
        except StopAsyncIteration:
            pass


if __name__ == "__main__":
    asyncio.run(main())
