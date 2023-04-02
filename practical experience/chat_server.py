# пример асинхронного мини-чата с использованием библиотеки asyncio и websockets.

# Cоздадим сервер:

import asyncio
import websockets


async def server(websocket, path):
    async for message in websocket:
        print(message)
        await websocket.send(message)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(websockets.serve(server, 'localhost', 8765))
    asyncio.get_event_loop().run_forever()


# Запустим сервер и подключимся к нему с помощью клиентов
