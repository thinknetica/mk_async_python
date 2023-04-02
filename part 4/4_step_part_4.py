# Пример работы с протоколом TCP:
import asyncio


async def handle_client(reader, writer):
    while True:
        data = await reader.read(1024)
        if not data:
            break
        message = data.decode()
        print(f"Received message: {message}")
        writer.write(data)
        await writer.drain()
    writer.close()


async def start_server():
    server = await asyncio.start_server(handle_client, 'localhost', 8888)
    async with server:
        await server.serve_forever()


async def connect():
    reader, writer = await asyncio.open_connection('localhost', 8888)
    message = "Hello, server!"
    writer.write(message.encode())
    await writer.drain()
    data = await reader.read(1024)
    response = data.decode()
    print(f"Received response: {response}")
    writer.close()
    await writer.wait_closed()


async def main():
    server_task = asyncio.create_task(start_server())
    await asyncio.sleep(1)
    client_task = asyncio.create_task(connect())
    await client_task
    server_task.cancel()

if __name__ == "__main__":
    asyncio.run(main())
