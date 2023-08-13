
import asyncio
import logging
import json
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# # from openaiManager import completion_endpoint_plain
# app = FastAPI()

# # Configure CORS
# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  # Replace with your frontend origin
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "OPTIONS"],
#     allow_headers=["*"],
# )
# # Configure CORS

# messages = []

# Configure logging format
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

# @app.get("/")
# def root():
#     if messages:
#         return {"message": messages[-1]}
#     else:
#         return {"message": "No messages yet"}

# @app.get("/api/messages")
# def get_messages():
#     return {"messages": "hello there"}


# @app.post("/api/messages")
# def add_message(message: dict):
#     new_message = message.get("message")
#     print("fdgdfgfdf fgfhf")
#     logging.info(f"Received new message: {new_message}")
#     messages.append(new_message)
#     # backend_response = completion_endpoint_plain(new_message)
#     return {"message": "\nimport sys\nsys.path.append('/path/to/folder')\nfrom my_module import my_function"}
#     # return {"message": backend_response}




from fastapi import FastAPI, WebSocket, HTTPException
from pydantic import BaseModel
import os

app = FastAPI()

class RepoLink(BaseModel):
    repoLink: str

@app.websocket("/ws/status")
async def status_websocket(websocket: WebSocket):
    await websocket.accept()
    logging.info(f"hello: ")
    try:
        while True:
            data = await websocket.receive_text()
            print("fdgdfgfdf fgfhf")
            logging.info(f"Received new message: ")
            message = {}
            if data:
                logging.info(f"Received new message: {data} ")

                repo_parts = "qwe"

                if len(repo_parts) != 2:
                    logging.info(f"Received chat message: ")

                    message['action'] = 'status'
                    message['message'] = 'Invalid link'
                    await websocket.send_json(message)
                else:
                    username, repo_name = repo_parts
                    # Perform the extraction and cloning here
                    try:
                        # Extract info
                        message['action'] = 'status'
                        message['message'] = 'Extraction complete'
                        await websocket.send_json(message)

                        # Clone the repository

                        message['action'] = 'status'
                        message['message'] = 'Cloned successfully'
                        await websocket.send_json(message)

                    except Exception as e:
                        message['action'] = 'status'
                        message['message'] = f'Error: {str(e)}'
                        await websocket.send_json(message)
    except Exception:
        pass




@app.websocket("/ws/chat")
async def chat_socket(websocket: WebSocket):
    await websocket.accept()
    logging.info(f"hello: ")
    try:
        while True:
            data = await websocket.receive_text()
            print("fdgdfgfdf fgfhf")
            logging.info(f"Received new message: ")
            query_data = json.loads(data)
            message = {}

            message['action'] = 'chat'
            message['message'] = 'valid link'
            message['chatId'] = query_data["chatId"]
            await websocket.send_json(message)
            await asyncio.sleep(8)
            if data:

                logging.info(f"Received new message: {data} ")

                repo_parts = "qwe"

                if len(repo_parts) != 2:
                    logging.info(f"Received chat message: ")

                    message['action'] = 'chat'
                    message['message'] = 'Invalid link'
                    message['chatId'] = query_data["chatId"]
                    await websocket.send_json(message)
                else:
                    username, repo_name = repo_parts
                    # Perform the extraction and cloning here
                    try:
                        # Extract info
                        message['action'] = 'status'
                        message['message'] = 'Extraction complete'
                        await websocket.send_json(message)

                        # Clone the repository

                        message['action'] = 'status'
                        message['message'] = 'Cloned successfully'
                        await websocket.send_json(message)

                    except Exception as e:
                        message['action'] = 'status'
                        message['message'] = f'Error: {str(e)}'
                        await websocket.send_json(message)
    except Exception:
        pass