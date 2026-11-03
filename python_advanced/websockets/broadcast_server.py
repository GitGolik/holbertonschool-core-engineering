#!/usr/bin/env python3
"""WebSocket server using broadcast communication."""

import asyncio

from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def broadcast(message: str):
    """Send a message to every currently connected client."""
    for client in list(connected_clients):
        try:
            await client.send(f"B:{message}")
        except ConnectionClosed:
            connected_clients.discard(client)


async def connection_handler(websocket):
    """Handle one client and broadcast its messages to all clients."""
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            await broadcast(message)
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    async with serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
