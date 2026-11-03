#!/usr/bin/env python3
"""ASGI WebSocket echo application with a browser client."""

from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import Mount, Route, WebSocketRoute
from starlette.staticfiles import StaticFiles


async def homepage(request):
    """Serve the browser client."""
    return FileResponse("index.html")


async def websocket_endpoint(websocket):
    """Echo every text message received on /ws."""
    await websocket.accept()

    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except Exception:
        pass


app = Starlette(
    routes=[
        Route("/", homepage),
        WebSocketRoute("/ws", websocket_endpoint),
        Mount("/static", app=StaticFiles(directory="."), name="static"),
    ]
)
