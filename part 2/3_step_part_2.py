import asyncio

import aiofiles


async def read_file_async(filename):
    async with aiofiles.open(filename, 'r') as f:
        return await f.read()


# asyncio.get_running_loop() - это функция, которая возвращает текущий event loop,
# который был запущен в текущем контексте исполнения.
# Если event loop не был запущен, то функция выбрасывает исключение RuntimeError.
# async def read_file_async(filename):
#     loop = asyncio.get_running_loop()
#     with open(filename, 'r') as f:
#         return await loop.run_in_executor(None, f.read)

async def main():
    print('Начало')
    result = await asyncio.gather(read_file_async('example.txt'))
    print('Конец:', result)


if __name__ == "__main__":
    asyncio.run(main())
