import asyncio


async def func():
    print("Function started")
    await asyncio.sleep(1)
    print("Function ended")


async def func_with_error():
    print("Function with error started")
    await asyncio.sleep(1)
    raise ValueError("Error in function with error")


async def handle_error(task):
    if task.exception():
        print(f"Error occurred in task {task}: {task.exception()}")


async def main():
    print("Main started")
    task1 = asyncio.create_task(func())
    task2 = asyncio.create_task(func_with_error())
    task3 = asyncio.create_task(func())
    for task in asyncio.all_tasks():
        task.add_done_callback(handle_error)
    await asyncio.gather(task1, task2, task3)
    print("Main ended")


if __name__ == "__main__":
    asyncio.run(main())
