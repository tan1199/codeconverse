
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



from clone_repo import extract_user_repo_github
from ast_parser import create_repo_ast
from fastapi import FastAPI, WebSocket, HTTPException, File, UploadFile
from pydantic import BaseModel
import os, re
import zipfile

from fastapi.responses import JSONResponse
app = FastAPI()
async def simulate_processing_stage_1():
    # Simulate some processing for stage 1
    await asyncio.sleep(1)

async def simulate_processing_stage_2():
    # Simulate some processing for stage 2
    await asyncio.sleep(1)

async def simulate_processing_stage_3():
    # Simulate some processing for stage 3
    await asyncio.sleep(1)
@app.websocket("/ws/process")
async def status_websocket(websocket: WebSocket):
    await websocket.accept()
    while True:
        progress_message = {}
        message = await websocket.receive_text()
        message_data = json.loads(message)
        filename = message_data.get('filename')
        print("llll",filename)
        if message_data['type'] == 'filename':
            data = await websocket.receive_bytes()  # Receive binary data in chunks
            await websocket.send_text(json.dumps({"action": "process", "message": f"{filename} Uploaded Successfully"}))
            if data:
                print("ertre")
                file_path=f'repositories/data/{filename}'
                # Process the received binary data as a chunk of a larger file
                with open(file_path, "ab") as f:
                    print("opop")
                    f.write(data)
                await asyncio.sleep(4)
                await websocket.send_text(json.dumps({"action": "process", "message":f"{filename} Processed Successfully"}))
                if filename.endswith('.zip'):
                    with zipfile.ZipFile(f'repositories/data/{filename}', 'r') as zip_ref:
                        zip_ref.extractall(f'repositories/data/')
                        print("Zip file extracted successfully.")
                    os.remove(file_path)
                    await asyncio.sleep(4)
                    await websocket.send_text(json.dumps({"action": "process", "message": "{filename} Extracted Successfully"}))
                await websocket.send_text(json.dumps({"type": "success"}))
                progress_message['action'] = 'process'
                progress_message['message'] = 'success'
                print(progress_message)
                await websocket.send_json(progress_message)
                await websocket.send_text(json.dumps({"action": "process", "message": "# Simulate some processing for stage 1"}))
                await simulate_processing_stage_1()  # Call your processing function
                await websocket.send_text(json.dumps({"action": "process", "message": "Stage 2              "}))
        elif message_data['type'] == 'url':
            source_url=message_data['url_string']
            if message_data['sourcetype'] == 'Github':
                pattern = r'https://github.com/([^/]+)/([^/]+)'
    
                    # Search for the pattern in the input URL
                await asyncio.sleep(4)
                await websocket.send_text(json.dumps({"action": "process", "message": "Search for the pattern in the input URL"}))
                
                match = re.search(pattern, source_url)
                print(match)
                if match:
                    # Extract the username and repo name from the matched groups
                    user_name = match.group(1)
                    repo_name = match.group(2)
                    if user_name and repo_name:
                        print("Username:", user_name)
                        print("Repository:", repo_name)
                        print(source_url)
                        await asyncio.sleep(1)
                        await websocket.send_text(json.dumps({"action": "process", "message": "Username and Repo name extracted Successfully"}))

                        extract_user_repo_github(source_url,user_name,repo_name)
                        await asyncio.sleep(2)
                        await websocket.send_text(json.dumps({"action": "process", "message": "GitHub Repository cloned Successfully"}))

                        print("nice")
                        await asyncio.sleep(3)
                        await websocket.send_text(json.dumps({"action": "process", "message": f"Parsing source code of {user_name}/{repo_name}"}))

                        create_repo_ast(f"{user_name}_{repo_name}")
                        await asyncio.sleep(4)
                        await websocket.send_text(json.dumps({"action": "process", "message": f" Source code of {user_name}/{repo_name} Parsed Successfully"}))
                        await asyncio.sleep(5)
                        await websocket.send_text(json.dumps({"data_source_name": f"{user_name}/{repo_name}","action": "process", "message": f" Data Source {user_name}/{repo_name} Successfully"}))


                        print("ioio")
                    else:
                        print("Invalid GitHub repository URL")
                        await asyncio.sleep(6)
                        await websocket.send_text(json.dumps({"action": "process", "message": "Invalid GitHub Repository URL"}))
        simulate_processing_stage_2()  # Call another processing function
        await websocket.send_text(json.dumps({"action": "process", "message": ""}))    
                          
    # aweeeeait websocket.accept()
    # await websocket.send_text("WebSocket connection established.")

    # file_data = bytearray()
    # while True:
    #     message = await websocket.receive_text()
    #     if message == "File upload complete":
    #         break
    #     file_data.extend(message.encode())  # Convert string message to bytes and extend bytearray

    # # Save the received file data to a file
    # file_path = os.path.join(UPLOAD_FOLDER, "data")
    # with file_path.open("wb") as f:
    #     f.write(file_data)

    # await websocket.send_text("File received and saved.")
    # await websocket.close()
    # await websocket.accept()
    # logging.info(f"hello: ")
    # try:
    #     while True:
    #         logging.info(f"hello1: ")
    #         file_data = await websocket.receive_text()
    #         logging.info(f"hello2: ")
    #         print(file_data)
    #         await websocket.send_text("File received and processed")

        # Process the received file data here
        # You can save it to a file or perform any other necessary actions

                # # await websocket.send_text(f"Received file name: {data}")
                # file_path = os.path.join(UPLOAD_FOLDER, "data")
                # print(file_path)
                # async with websocket.stream(filename=file_path) as upload_file:
                #     await shutil.copyfileobj(upload_file, open(file_path, "wb"))

                # repo_parts = "qwe"

                # if len(repo_parts) != 2:
                #     logging.info(f"Received chat message: ")

                #     message['action'] = 'status'
                #     message['message'] = 'Invalid link'
                #     await websocket.send_json(message)
                # else:
                #     username, repo_name = repo_parts
                #     # Perform the extraction and cloning here
                #     try:
                #         # Extract info
                #         message['action'] = 'status'
                #         message['message'] = 'Extraction complete'
                #         await websocket.send_json(message)

                #         # Clone the repository

                #         message['action'] = 'status'
                #         message['message'] = 'Cloned successfully'
                #         await websocket.send_json(message)

                #     except Exception as e:
                #         message['action'] = 'status'
                #         message['message'] = f'Error: {str(e)}'
                #         await websocket.send_json(message)
    # except Exception:
    #     pass




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
                    # await asyncio.sleep(20)

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