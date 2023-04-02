import asyncio


async def coro1():
    print("Starting coro1")
    await asyncio.sleep(2)
    raise ValueError("Error in coro1")


async def coro2():
    print("Starting coro2")
    await asyncio.sleep(3)
    print("Ending coro2")


async def main():
    # tasks = [asyncio.ensure_future(coro1()), asyncio.ensure_future(coro2())]
    tasks = [asyncio.create_task(coro1()), asyncio.create_task(coro2())]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)

    for task in done:
        try:
            result = await task
        except Exception as e:
            print(f"Error in {task}: {e}")
        else:
            print(f"{task} completed: {result}")

if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    asyncio.run(main())

