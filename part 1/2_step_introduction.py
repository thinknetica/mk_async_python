import asyncio


async def long_operation():
    print("Starting long operation")
    await asyncio.sleep(5)
    print("Long operation completed")


async def main():
    print("Start")
    task = asyncio.create_task(long_operation())
    await task
    print("End")


if __name__ == "__main__":
    asyncio.run(main())
