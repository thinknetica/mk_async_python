import asyncio
import time


# блокирующая операция чтения файла в асинхронном коде

def read_file(filename):
    with open(filename, 'r') as f:
        time.sleep(5)  # имитация долгой операции чтения файла
        return f.read()


async def main():
    print('Начало')
    result = await asyncio.gather(read_file('example.txt'))  # асинхронное чтение файла
    print('Конец:', result)


if __name__ == "__main__":
    asyncio.run(main())
