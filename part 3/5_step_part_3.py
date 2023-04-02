import asyncio


async def my_async_function():
    print("Start")
    await asyncio.sleep(1)
    print("End")


async def my_coroutine():
    print("Before")
    await my_async_function()
    print("After")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(my_coroutine())
    loop.close()
    # или так запускать корутины в Python 3.7+ (без создания event loop)
    # asyncio.run(my_coroutine())


