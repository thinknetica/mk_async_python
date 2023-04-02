import asyncio


async def coro():
    await asyncio.sleep(1)
    print("Hello")
    return "Result"


async def main():
    # Создаем объект Future
    fut = asyncio.Future()

    # Создаем объект Task
    task = asyncio.create_task(coro())

    # Получаем результат из объекта Future
    result = await fut

    # Получаем результат из объекта Task
    result = await task


if __name__ == "__main__":
    asyncio.run(main())
