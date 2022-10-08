from fastapi import APIRouter
from fastapi import WebSocket

router = APIRouter(prefix="/chat", tags=["Chat"], responses={404: {"description": "Not found"}})


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
