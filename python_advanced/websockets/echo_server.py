#!/usr/bin/env python3
"""Minimal WebSocket echo server."""

import asyncio

import websockets


async def connection_handler(websocket, path=None):
    """Echo every text message received from one client."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
