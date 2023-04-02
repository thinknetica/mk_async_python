# Теперь, создадим клиент:

import asyncio
import websockets


async def client():
    async with websockets.connect('ws://localhost:8765') as websocket:
        await websocket.send('Hello, server! I am client 3')
        response = await websocket.recv()
        print(response)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(client())
