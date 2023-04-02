import asyncio


async def some_task():
    await asyncio.sleep(1)
    return "Task completed"


async def main():
    task = asyncio.create_task(some_task())
    task.add_done_callback(callback)
    print(task.done())  # False
    task.cancel()
    print(task.done())  # True
    try:
        await task
    except asyncio.CancelledError:
        print("Task was cancelled")
    else:
        print(task.result())  # This line will not be reached
    print(task.exception())  # None
    task.set_result("New result")
    print(task.result())  # "New result"
    task.set_exception(ValueError("New error"))
    print(task.exception())  # ValueError("New error")


def callback(future):
    print("Callback called")


if __name__ == "__main__":
    asyncio.run(main())
