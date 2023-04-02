import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://example.com')
        print(html)


if __name__ == "__main__":
    asyncio.run(main())
