import asyncio


async def func():
    print("Function started")
    await asyncio.sleep(1)
    print("Function ended")


async def func_with_error():
    print("Function with error started")
    await asyncio.sleep(1)
    raise ValueError("Error in function with error")


async def main():
    print("Main started")
    tasks = [asyncio.create_task(func()), asyncio.create_task(func_with_error()), asyncio.create_task(func())]
    await asyncio.gather(*tasks)
    print("Main ended")


if __name__ == "__main__":
    asyncio.run(main())
