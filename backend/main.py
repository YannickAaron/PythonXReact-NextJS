import uvicorn as uvicorn
from fastapi import FastAPI

from fastapi.responses import HTMLResponse

from pythonxreact.config.celery_utils import create_celery
from pythonxreact.routers import universities, chat

from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    current_app = FastAPI(
        title="Asynchronous tasks processing with Celery and RabbitMQ",
        description="Sample FastAPI Application to demonstrate Event " "driven architecture with Celery and RabbitMQ",
        version="1.0.0",
    )

    current_app.celery_app = create_celery()  # create celery app instance
    current_app.include_router(universities.router)
    current_app.include_router(chat.router)
    return current_app


app = create_app()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # can alter with time
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

celery = app.celery_app

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:9000/chat/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)
