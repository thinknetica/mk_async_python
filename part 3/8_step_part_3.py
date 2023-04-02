import asyncio


async def task():
    await asyncio.sleep(1)
    raise Exception("Something went wrong")


async def main():
    try:
        task_future = asyncio.ensure_future(task())
        await asyncio.sleep(0.5)
        await asyncio.shield(task_future)  # Защищаем задачу от отмены во время ожидания
    except Exception as e:
        print("Error occurred:", e)


if __name__ == "__main__":
    asyncio.run(main())
