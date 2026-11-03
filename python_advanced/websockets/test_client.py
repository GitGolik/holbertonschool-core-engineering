#!/usr/bin/env python3
"""Test client for the WebSocket echo server."""

import asyncio

import websockets


async def main():
    uri = "ws://127.0.0.1:8765/"

    async with websockets.connect(uri) as websocket:
        message = "Hello"

        print(f"Client sent: {message}")
        await websocket.send(message)

        response = await websocket.recv()
        print(f"Client received: {response}")

        if response == message:
            print("Echo OK")
        else:
            print("Echo FAILED")


if __name__ == "__main__":
    asyncio.run(main())
