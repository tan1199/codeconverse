
import asyncio
import logging
import json
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from openaiManager import completion_endpoint_plain
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
            message['progressbar'] = True

            # await websocket.send_json(message)
            # await asyncio.sleep(8)
            if data:

                logging.info(f"Received new message: {data} ")

                repo_parts = "qwe"

                if len(repo_parts) != 2:
                    logging.info(f"Received chat message: ")
               
#                     backend_response = """
# In Java, the `TypeReference` class is used to capture the generic type information at runtime. It is commonly used when working with libraries or frameworks that require generic type information, such as JSON parsing libraries like Jackson or Gson.

# Here's an example of how to use `TypeReference` in Java:

# 1. Import the necessary classes:
# ```java
# import com.fasterxml.jackson.core.type.TypeReference;
# import com.fasterxml.jackson.databind.ObjectMapper;
# ```

# 2. Create an instance of `ObjectMapper`:
# ```java
# ObjectMapper objectMapper = new ObjectMapper();
# ```

# 3. Define a generic type using `TypeReference`:
# ```java
# TypeReference<List<String>> typeReference = new TypeReference<List<String>>() {};
# ```
# In this example, we are defining a `TypeReference` for a `List` of `String` objects.

# 4. Use the `ObjectMapper` to read or write JSON data:
# ```java
# String json = "[\"apple\", \"banana\", \"orange\"]";

# try {
#     List<String> fruits = objectMapper.readValue(json, typeReference);
#     System.out.println(fruits); // Output: [apple, banana, orange]
# } catch (IOException e) {
#     e.printStackTrace();
# }
# ```
# In this example, we are using the `readValue()` method of `ObjectMapper` to parse the JSON string into a `List` of `String` objects, using the `TypeReference` to preserve the generic type information.

# Note that the `TypeReference` is an abstract class, so we need to create an anonymous subclass by using `{}` at the end of the declaration.

# By using `TypeReference`, we can work with generic types at runtime without losing the type information.
# fgdfgd

# """     
                    backend_response = completion_endpoint_plain(query_data["data"])
                    print(query_data["data"],backend_response)
                    message['action'] = 'chat'
                    message['message'] = backend_response
                    message['chatId'] = query_data["chatId"]
                    message['newvalue'] = "acha"
                    message['progressbar'] = False

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