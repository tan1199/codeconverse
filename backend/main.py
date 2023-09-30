
import asyncio
import logging
import json
# from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openaiManager import completion_endpoint_plain
# app = FastAPI()

# # Configure CORS
# app = FastAPI()



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

from connect_db import insert_message,select_all_chats,deletechatId,insert_user,select_user
import time,sqlite3
from clone_repo import extract_user_repo_github
from ast_parser import create_repo_ast,create_upload_ast,language_extensions_to_class_attribute,language_extensions_to_function_attribute,class_attributes,function_attributes
from fastapi import FastAPI, WebSocket, HTTPException, File, UploadFile, Depends, status,WebSocketDisconnect
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from pydantic import BaseModel
import os, re,shutil
import zipfile
import pandas as pd
from pathlib import Path
from prompts import metadata_json_prompt
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json
import jwt
import Levenshtein
from rapidfuzz import fuzz
from similarity_search import calculate_levenshtein_fuzzy_distance_similarity,code_embedding_similarity_search
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your frontend origin
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)
# Configure CORS

no_Df=True
# df = pd.DataFrame(columns=["code_chunk", "file_name", "file_path", "path_to_code_chunk","parent","prev_sibling","next_sibling","start_point","end_point","has_error","code_node_type","code_identifier","is_chunked","num_tokens","uuid_str"])

async def simulate_processing_stage_1():
    # Simulate some processing for stage 1
    await asyncio.sleep(1)

async def simulate_processing_stage_2():
    # Simulate some processing for stage 2
    await asyncio.sleep(1)

async def simulate_processing_stage_3():
    # Simulate some processing for stage 3
    await asyncio.sleep(1)


# Define your JWT secret key (replace with a strong, random key)
SECRET_KEY = "your-secret-key354354gfbgc@354gfbkhjyiyuWREF#56TcdsERD7vxc"

# Define the algorithm used for JWT (HS256 is a common choice)
ALGORITHM = "HS256"

# Define the access token expiration time (in minutes)
ACCESS_TOKEN_EXPIRE_MINUTES = 10

# Mock user database for demonstration
fake_users_db = {
    "user1": {
        "username": "user1",
        "password": "password1",
    }
}

# OAuth2 Bearer Token scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
class UserInfo(BaseModel):
    username: str
    password: str
    email_id: str
    isSignup: bool
    google_auth: bool
# Function to create an access token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Function to verify and decode a JWT token
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            return None
        return username
    except Exception as e:
        return None

# Function to verify user credentials and return user details
def get_current_user(token: str = Depends(oauth2_scheme)):
    # Verify the token
    print("ojo",token)
    username = verify_token(token)
    print("lala",username)
    if username is None:
        return username
        # raise HTTPException(
        #     status_code=status.HTTP_401_UNAUTHORIZED,
        #     detail="Invalid token",
        #     headers={"WWW-Authenticate": "Bearer"},
        # )
    
    # Retrieve user details from the mock database
    user = select_user(username)
    print(user)
    # if user is None:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="User not found",
    #         headers={"WWW-Authenticate": "Bearer"},
    #     )

    return user

# Route to obtain an access token
@app.post("/token", response_model=dict)
async def login_for_access_token(form_data: dict):
    username = form_data["username"]
    password = form_data["password"]
    email_id = form_data["email_id"]
    isSignup = form_data["isSignup"]
    google_auth = form_data["google_auth"]
    insert_status="user_registered"
    if isSignup == False:
        user = select_user(username)
        print("HHJK",user)
        if user is None or user["password"] != password:
            if google_auth:
                insert_status=insert_user(username,password, email_id, 'https://example.com/avatar.png', int(time.time() * 1000)) 

            else:
                raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
                headers={"WWW-Authenticate": "Bearer"},
                )
    else:
        insert_status=insert_user(username,password, email_id, 'https://example.com/avatar.png', int(time.time() * 1000)) 
        print("ellls",insert_status)
    # Generate an access token
    if insert_status=="user_registered":
        access_token = create_access_token(data={"sub": username})
    else:
        access_token=None

    return {"access_token": access_token, "token_type": "bearer","insert_status":insert_status}
# Protected route that requires authentication
@app.get("/protected")
async def protected_route(user: dict = Depends(get_current_user)):
    return {"message": "This is a protected route", "user": user}


@app.websocket("/ws/user")
async def userdetail_websocket(websocket: WebSocket):
    user = get_current_user(websocket.query_params.get("token"))
    print("nanan",user)
    await websocket.accept()
    print("rdytj")
    if not user:
            # Token has expired or is invalid, handle reauthentication
            # You can send a message to the client to trigger reauthentication
            # await websocket.send_text("Your token has expired. Please reauthenticate.")
            print("loal")
            # Close the WebSocket connection
            await websocket.close()

    # await websocket.send_text(json.dumps({"user_data":user}))


@app.websocket("/ws/initiate")
async def initiate_websocket(websocket: WebSocket):
    try:
        conversation_data1 = [{'chatId': '1692436170698', 'messages': [{'id': 1692436175759, 'avatar': 'https://example.com/avatar.png', 'username': 'User', 'message': 'hello', 'timestamp': 1692436175759}, {'id': 1692436181744, 'avatar': 'https://example.com/avatar.png', 'username': 'AI Assistant', 'message': 'Hello! How can I assist you today?', 'timestamp': 1692436181744}, {'id': 1692436191162, 'avatar': 'https://example.com/avatar.png', 'username': 'User', 'message': 'how are you', 'timestamp': 1692436191162}, {'id': 1692436198048, 'avatar': 'https://example.com/avatar.png', 'username': 'AI Assistant', 'message': "As an AI, I don't have feelings, but I'm here to help you with any questions or tasks you have. How can I assist you today?", 'timestamp': 1692436198048}, {'id': 1692436211157, 'avatar': 'https://example.com/avatar.png', 'username': 'User', 'message': 'what is the capital of denmark', 'timestamp': 1692436211157}, {'id': 1692436216969, 'avatar': 'https://example.com/avatar.png', 'username': 'AI Assistant', 'message': 'The capital of Denmark is Copenhagen.', 'timestamp': 1692436216969}, {'id': 1692436225940, 'avatar': 'https://example.com/avatar.png', 'username': 'User', 'message': 'best cricker of world', 'timestamp': 1692436225940}, {'id': 1692436233668, 'avatar': 'https://example.com/avatar.png', 'username': 'AI Assistant', 'message': 'There have been many great cricketers throughout history, and it is subjective to determine the best cricketer of all time. However, some of the most highly regarded cricketers include Sir Donald Bradman, Sachin Tendulkar, Sir Vivian Richards, Sir Garfield Sobers, and Sir Jack Hobbs. These players have achieved remarkable records and have left a lasting impact on the game of cricket.', 'timestamp': 1692436233668}]}, {'chatId': '1692436239709', 'messages': []}, {'chatId': '1692436243005', 'messages': [{'id': 1692436251519, 'avatar': 'https://example.com/avatar.png', 'username': 'User', 'message': 'some icream flovors', 'timestamp': 1692436251519}, {'id': 1692436259952, 'avatar': 'https://example.com/avatar.png', 'username': 'AI Assistant', 'message': '1. Vanilla\n2. Chocolate\n3. Strawberry\n4. Mint chocolate chip\n5. Cookies and cream\n6. Butter pecan\n7. Rocky road\n8. Coffee\n9. Pistachio\n10. Salted caramel\n11. Neapolitan\n12. Cherry Garcia (cherry ice cream with chocolate chunks and cherries)\n13. Peanut butter cup\n14. Coconut\n15. Birthday cake\n16. Matcha green tea\n17. Black raspberry\n18. Dulce de leche\n19. Red velvet\n20. Lemon sorbet', 'timestamp': 1692436259952}, {'id': 1692436267399, 'avatar': 'https://example.com/avatar.png', 'username': 'User', 'message': 'different color of apple', 'timestamp': 1692436267399}, {'id': 1692436279132, 'avatar': 'https://example.com/avatar.png', 'username': 'AI Assistant', 'message': 'There are several different colors of apples, including:\n\n1. Red: This is the most common color for apples, with varieties such as Red Delicious, Gala, and Fuji.\n\n2. Green: Green apples, such as Granny Smith and Golden Delicious, have a tart flavor and are often used in baking or for making apple cider.\n\n3. Yellow: Yellow apples, like Yellow Transparent and Yellow Newtown Pippin, have a sweet and tangy taste.\n\n4. Pink: Pink Lady apples have a distinctive pinkish-red skin and a crisp, sweet-tart flavor.\n\n5. Bi-colored: Some apples have a combination of colors, such as the popular Honeycrisp apple, which has a red and yellow skin.\n\n6. Striped: Certain apple varieties, like the McIntosh apple, have a striped pattern on their skin, with a mix of red and green.\n\n7. Purple: There are a few varieties of purple apples, such as the Black Diamond apple, which have a deep purple or almost black skin.\n\nThese are just a few examples of the different colors of apples available. The specific color and appearance of an apple can vary depending on the variety and ripeness.', 'timestamp': 1692436279132}, {'id': 1692436280326, 'avatar': 'https://example.com/avatar.png', 'username': 'User', 'message': 'japan to india distance', 'timestamp': 1692436280326}, {'id': 1692436286987, 'avatar': 'https://example.com/avatar.png', 'username': 'AI Assistant', 'message': 'The distance between Japan and India is approximately 4,500 kilometers (2,800 miles) when measured in a straight line. However, the actual distance may vary depending on the route taken for travel.', 'timestamp': 1692436286987}, {'id': 1692436288296, 'avatar': 'https://example.com/avatar.png', 'username': 'User', 'message': 'bye bye', 'timestamp': 1692436288296}, {'id': 1692436294137, 'avatar': 'https://example.com/avatar.png', 'username': 'AI Assistant', 'message': 'Goodbye! Have a great day!', 'timestamp': 1692436294137}]}]
        conversation_data = select_all_chats()
        # print(conversation_data)

        user = get_current_user(websocket.query_params.get("token"))
        print("acdf",user)
        await websocket.accept()
        print("rdytj")
        if not user:
            # Token has expired or is invalid, handle reauthentication
            # You can send a message to the client to trigger reauthentication
            # await websocket.send_text("Your token has expired. Please reauthenticate.")
            await websocket.send_text(json.dumps({"authentication":False}))

            print("loal")
            # Close the WebSocket connection
            await websocket.close()

        # await asyncio.sleep(1)
        # await websocket.send_text("Hello  now from FastAPI!")
        else:
            file_list = []
            root1 = Path(__file__).parent
            input_directory_path = f"{root1}/repositories"  # Replace with the actual path to your directory
            file_list = [f.split('.')[0] for f in os.listdir(input_directory_path) if f not in ['data','final']] 
            # for filename in os.listdir(csv_directory_path):
            #     if filename.endswith(".csv"):
            #         csv_files.append(os.path.splitext(filename)[0])
            print(file_list)       
            await websocket.send_text(json.dumps({"username":user["username"],"chat_data":conversation_data,"saved_data_source":file_list,"action": "initiate", "message": "Uploaded Successfully"}))


        # while True:
        # # progress_message = {}
        #     message = await websocket.receive_text()
        #     print(message)
    except WebSocketDisconnect:
        pass
def delete_files_with_string(root_dir, target_string):
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isfile(item_path) and target_string in item:
            os.remove(item_path)
            print(f"Deleted file: {item_path}")
        elif os.path.isdir(item_path) and target_string in item:
            try:
                shutil.rmtree(item_path)
                print(f"Deleted directory and its contents: {item_path}")
            except Exception as e:
                 print(f"Error while deleting directory: {e}")

@app.websocket("/ws/process")
async def status_websocket(websocket: WebSocket):
    user = get_current_user(websocket.query_params.get("token"))
    print("nanan",user)
    await websocket.accept()
    print("rdytj")
    if not user:
            # Token has expired or is invalid, handle reauthentication
            # You can send a message to the client to trigger reauthentication
            # await websocket.send_text("Your token has expired. Please reauthenticate.")
        print("loal")
            # Close the WebSocket connection
        await websocket.close()

        # await asyncio.sleep(1)
        # await websocket.send_text("Hello  now from FastAPI!")
    else:

        try:
            while True:
                progress_message = {}
                message = await websocket.receive_text()
                message_data = json.loads(message)
                filename = message_data.get('filename')
                print("llll",filename)
                if message_data['type'] == 'deletedatasource':
                    if "." in filename:
                        filename=filename.split('.')[0]
                    root2 = Path(__file__).parent
                    root_directory=f'{root2}/repositories/{filename}.csv'
                    if os.path.exists(root_directory):
                        os.remove(root_directory)   
                    print("olhg")
                    root_directory=f'{root2}/repositories/data'   
                    delete_files_with_string(root_directory, filename)
                    print("rtyvj")

                elif message_data['type'] == 'deletechatId':
                    print("del begin")
                    print("ttyyp",type(filename))
                    deletechatId(filename)
                    print("delte end")
                elif message_data['type'] == 'filename':
                    data = await websocket.receive_bytes()  # Receive binary data in chunks
                    await websocket.send_text(json.dumps({"action": "process", "message": f"{filename} Uploaded Successfully"}))
                    if data:
                        # print("ertre")
                        file_path=f'repositories/data/{filename}'
                        # print("wwwwww")
                        if os.path.exists(file_path) or os.path.exists(file_path.split('.')[0]):
                            # print("qqqqqqqqqqq")
                            await asyncio.sleep(2)
                            await websocket.send_text(json.dumps({"action": "process", "message":f"{filename} Exists"}))
                            await asyncio.sleep(2)
                            await websocket.send_text(json.dumps({"action": "process", "message":""}))
                            continue
                        # Process the received binary data as a chunk of a larger file
                        with open(file_path, "ab") as f:
                            # print("opop")
                            f.write(data)
                        await asyncio.sleep(2)
                        await websocket.send_text(json.dumps({"action": "process", "message":f"{filename} Processed Successfully"}))
                        if filename.endswith('.zip'):
                            with zipfile.ZipFile(f'repositories/data/{filename}', 'r') as zip_ref:
                                zip_ref.extractall(f'repositories/data/')
                                print("Zip file extracted successfully.")
                            os.remove(file_path)
                            await asyncio.sleep(2)
                            await websocket.send_text(json.dumps({"action": "process", "message": f"Zip File Extracted Successfully"}))
                        # await websocket.send_text(json.dumps({"type": "success"}))
                        await asyncio.sleep(2)
                        await websocket.send_text(json.dumps({"action": "process", "message": f"Parsing source code of {filename}"}))

                        create_upload_ast(filename,file_path)
                        await asyncio.sleep(2)
                        await websocket.send_text(json.dumps({"action": "process", "message": f" Source code of {filename} Parsed Successfully"}))
                        await asyncio.sleep(2)
                        await websocket.send_text(json.dumps({"data_source_name": f"{filename}","action": "process", "message": f" Data Source {filename} Successfully"}))
                elif message_data['type'] == 'url':
                    source_url=message_data['url_string']
                    if message_data['sourcetype'] == 'Github':
                        pattern = r'https://github.com/([^/]+)/([^/]+)'
            
                            # Search for the pattern in the input URL                
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
                                await websocket.send_text(json.dumps({"action": "process", "message": "Repository Metadata extracted Successfully"}))
                                print("wwwwww")
                                root1 = Path(__file__).parent
                                file_path1=f'{root1}/repositories/{user_name}_{repo_name}.csv'
                                if os.path.exists(file_path1):
                                    print("qqqqqqqqqqq")
                                    await asyncio.sleep(2)
                                    await websocket.send_text(json.dumps({"action": "process", "message":f"{user_name}_{repo_name} Exists"}))
                                    await asyncio.sleep(4)
                                    await websocket.send_text(json.dumps({"action": "process", "message":""}))
                                    continue
                                extract_user_repo_github(source_url,user_name,repo_name)
                                await asyncio.sleep(2)
                                await websocket.send_text(json.dumps({"action": "process", "message": "GitHub Repository cloned Successfully"}))

                                print("nice")
                                await asyncio.sleep(2)
                                await websocket.send_text(json.dumps({"action": "process", "message": f"Parsing source code of {user_name}/{repo_name}"}))

                                create_repo_ast(f"{user_name}_{repo_name}")
                                await asyncio.sleep(2)
                                await websocket.send_text(json.dumps({"action": "process", "message": f" Source code of {user_name}/{repo_name} Parsed Successfully"}))
                                await asyncio.sleep(2)
                                await websocket.send_text(json.dumps({"data_source_name": f"{user_name}_{repo_name}","action": "process", "message": f" Data Source {user_name}/{repo_name} Successfully"}))

                            else:
                                await asyncio.sleep(2)
                                await websocket.send_text(json.dumps({"action": "process", "message": "Invalid GitHub Repository URL"}))
                # simulate_processing_stage_2()  # Call another processing function
                await asyncio.sleep(5)
                await websocket.send_text(json.dumps({"action": "process", "message": ""}))    
        except WebSocketDisconnect:
            pass  

@app.websocket("/ws/chat")
async def chat_socket(websocket: WebSocket):
    global no_Df
    user = get_current_user(websocket.query_params.get("token"))
    print("nanan",user)
    await websocket.accept()
    print("rdytj")
    if not user:
            # Token has expired or is invalid, handle reauthentication
            # You can send a message to the client to trigger reauthentication
            # await websocket.send_text("Your token has expired. Please reauthenticate.")
        print("loal")
            # Close the WebSocket connection
        await websocket.close()
        return
    try:
        while True:
            data = await websocket.receive_text()
            if data:
                  query_data = json.loads(data)
                  if query_data["type"]=="activate":
                      print(query_data["active_df"])
                      root = Path(__file__).parent
                      if len(query_data["active_df"])!=0:
                        no_Df=False
                        data_frame=query_data["active_df"][0]
                        print("asouter")
                        print(f"{root}/repositories/{data_frame}.csv")
                        df=pd.read_csv(f"{root}/repositories/{data_frame.split('.')[0]}.csv")
                        print("outer")
                        for i in range(1, len(query_data["active_df"])):
                            print("Inner")
                            data_frame = query_data["active_df"][i]
                            print("olko",data_frame)
                            print(f"{root}/repositories/{data_frame.split('.')[0]}.csv")
                            df1=pd.read_csv(f"{root}/repositories/{data_frame.split('.')[0]}.csv")
                            df = pd.concat([df, df1], ignore_index=True)
                            print(df)
                            print("nowu")
                            print(df1)
                        df.to_csv(f"{root}/repositories/final/qwe.csv", index=False)                      
                      else :
                          no_Df=True
                  elif query_data["type"]=="chat":
                    start_time = time.time()  # Record the start time
                    print(query_data["metadata_filter"])
                    refined_response=""
                    user_prompt=query_data["data"]
                    conversation_data1 = query_data["ch"]
                    selectedid = query_data["chatId"]
                    chat_history="Chat History: []"
                    filtered_conversations = [conversation for conversation in conversation_data1 if conversation['chatId'] == selectedid]
                    if filtered_conversations:
                        last_conversation = filtered_conversations[-1]
                        last_4_messages = last_conversation['messages'][-4:]
                        last_4_message_texts = [message['message'] for message in last_4_messages]
                        if len(last_4_message_texts)==2:
                            chat_history=f"""Chat History:
User: {last_4_message_texts[0]}
Assistant: {last_4_message_texts[1]} 

        """
                        elif len(last_4_message_texts)==4:
                            chat_history=f"""Chat History:
User  {last_4_message_texts[0]}]
Assistant: {last_4_message_texts[1]}]   

User: {last_4_message_texts[2]}]
Assistant: {last_4_message_texts[3]}]    

        """        
                    print(chat_history,no_Df)
                    code_context=""
                    code_search_prompt=chat_history
                    file_name_value=class_value=funcion_value="NA"

                    if no_Df==False and query_data["metadata_filter"]:
                        prompt=metadata_json_prompt+f"user query :'{user_prompt}"
                        llm_json_response = completion_endpoint_plain(prompt)
                        print(llm_json_response)
                        try:
                            instruction_data = json.loads(llm_json_response)
                            i=0
                            code_context=""
                            for instruction_obj in instruction_data['instructions']:
                                instruction = instruction_obj['instruction']
                                command = instruction_obj['command']
                                metadata = instruction_obj['metadata']
                                additional_info = instruction_obj['additional_info']
                                target_function_value = instruction_obj['metadata']['function_name']
                                target_class_value = instruction_obj['metadata']['class_name']
                                target_file_value = instruction_obj['metadata']['file_name']
                                print("dss",target_file_value)
                                print("After JSON parsing (if successful)")
                                file_name_value=class_value=funcion_value="NA"
                                filtered_df=df
                                if target_file_value !="NA":
                                    filtered_df['file_similarity_score'] = filtered_df['file_name'].apply(calculate_levenshtein_fuzzy_distance_similarity,target_value=target_file_value)
                                    min_score=filtered_df['file_similarity_score'].min()
                                    print("file",min_score)
                                    if min_score<3:
                                        file_name_value_row = filtered_df[filtered_df['file_similarity_score'] == min_score]
                                        file_name_value = file_name_value_row['file_name'].values[0]


                                if target_class_value !="NA":
                                    mask=filtered_df['code_node_type'].isin(class_attributes)
                                    if file_name_value!="NA":
                                        mask=filtered_df['code_node_type'].isin(language_extensions_to_class_attribute[file_name_value.split('.')[1]])
                                    filtered_df.loc[mask,'class_similarity_score'] = filtered_df['code_identifier'].apply(calculate_levenshtein_fuzzy_distance_similarity,target_value=target_class_value)
                                    min_score=filtered_df['class_similarity_score'].min()
                                    print("class",min_score)

                                    if min_score<3:
                                        class_value_row = filtered_df[filtered_df['class_similarity_score'] == min_score]
                                        class_value = class_value_row['code_identifier'].values[0]

                                if target_function_value !="NA":
                                    mask=filtered_df['code_node_type'].isin(function_attributes)
                                    if file_name_value!="NA":
                                        mask=filtered_df['code_node_type'].isin(language_extensions_to_function_attribute[file_name_value.split('.')[1]])
                                   
                                    filtered_df.loc[mask,'funcion_similarity_score'] = filtered_df['code_identifier'].apply(calculate_levenshtein_fuzzy_distance_similarity,target_value=target_function_value)
                                    min_score=filtered_df['funcion_similarity_score'].min()
                                    print("func",min_score)
                                    if min_score<3:
                                        funcion_value_row = filtered_df[filtered_df['funcion_similarity_score'] == min_score]
                                        print("hgbj",funcion_value_row)
                                        funcion_value = funcion_value_row['code_identifier'].values[0]
                                print(file_name_value,class_value,funcion_value)
                                print("SDFS")
                                if file_name_value!="NA":
                                    filtered_df = filtered_df[filtered_df['file_name']==file_name_value]
                                    print("iop",filtered_df)
                                if class_value!="NA" and funcion_value!="NA":
                                    filtered_df = filtered_df[(filtered_df['code_identifier'] == funcion_value) &
    (
        filtered_df['path_to_code_chunk'].str.contains(f"/class_definition-{class_value}/") |
        filtered_df['path_to_code_chunk'].str.contains(f"/decorated_definition-{class_value}/") |
        filtered_df['path_to_code_chunk'].str.contains(f"/class_declaration-{class_value}/") |
        filtered_df['path_to_code_chunk'].str.contains(f"/class_specifier-{class_value}/") |
        filtered_df['path_to_code_chunk'].str.contains(f"/impl_item-{class_value}/")
    )
]                                   
                                    print("cls",filtered_df)                                
                                elif class_value!="NA":
                                    filtered_df = filtered_df[filtered_df['code_identifier']==class_value]
                                elif funcion_value!="NA":
                                  print("bji",filtered_df)
                                  filtered_df = filtered_df[filtered_df['code_identifier']==funcion_value]
                                  print("plo",filtered_df)

                                context_result,similarity,file_ext=code_embedding_similarity_search(filtered_df,instruction)
                                code_context += f"Code Snippet for {instruction} : \n"+context_result+"\n"
                                print("yuiop",instruction,code_context)
                            code_search_prompt+=f"""
{code_context}

User Query: {user_prompt}

Assistant Response:
[Begin your response here. Craft a comprehensive and insightful answer that addresses the user query by integrating relevant information from the code context, chat history, or both,REMEMBER NEVER provide the entire code context block at the end of your response just use it if needed to answer query . Prioritize the most pertinent source based on factors such as user query relevance, sequential flow of conversation, code complexity, and user intent. Refrain from duplicating the user query in your response. Tailor your answer to the user's needs while maintaining a coherent and informative narrative.

Utilize code context when it directly pertains to the user query or if the query concerns a specific code snippet. If the user query builds upon prior conversation, incorporating relevant parts of the chat history might be more suitable.

Strive to strike a balance between code context and chat history, focusing on the source that offers the most clarity for the user's query.

If the available information is inadequate, kindly acknowledge it and guide the user on seeking further information.
Finally  do ouptut the following string based on if you utilized the code context in formulating your answer or not 
(code_context_utilized: "YES/NO")]

"""
                                # print(code_search_prompt)
                            refined_response =completion_endpoint_plain(code_search_prompt)
                            print("ijjij",refined_response)
                            lines = refined_response.split('\n')
                            last_line = lines[-1].strip()
                            print("nmnmnm",last_line,file_ext)
                            if ("YES" in last_line and similarity>0.741) or ( ( file_name_value!="NA" ) or ( class_value !="NA" ) or ( funcion_value!= "NA" ) ):
                                lines[-1] = f"{code_context}"     
                                print(" 88888888888888888 ",lines[-1]) 
                                refined_response= '\n'.join(lines)
                            else:
                                lines.pop()  
                                refined_response= '\n'.join(lines)
                                       

                        except json.JSONDecodeError as e:
                            print("JSON Decode Error:", e)
                            
                    elif no_Df==False:
                        print("lainla",len(df),code_context,"nknkk",chat_history)
                        context_result,similarity,file_ext = code_embedding_similarity_search(df,user_prompt)
                        code_context += f"Code Snippet for {user_prompt} : \n"+context_result+"\n"
                        print("pnofil ",user_prompt,code_context)
                        # print("yuiop",instruction,code_context)
                        code_search_prompt+=f"""
{code_context}

User Query: {user_prompt}

Assistant Response:
[Begin your response here. Craft a comprehensive and insightful answer that addresses the user query by integrating relevant information from the code context, chat history, or both,REMEMBER NEVER provide the entire code context block at the end of your response just use it if needed to answer query . Prioritize the most pertinent source based on factors such as user query relevance, sequential flow of conversation, code complexity, and user intent. Refrain from duplicating the user query in your response. Tailor your answer to the user's needs while maintaining a coherent and informative narrative.

Utilize code context when it directly pertains to the user query or if the query concerns a specific code snippet. If the user query builds upon prior conversation, incorporating relevant parts of the chat history might be more suitable.

Strive to strike a balance between code context and chat history, focusing on the source that offers the most clarity for the user's query.

If the available information is inadequate, kindly acknowledge it and guide the user on seeking further information.
Finally  do ouptut the following string based on if you utilized the code context in formulating your answer or not 
(code_context_utilized: "YES/NO")]

"""                     
                        refined_response =completion_endpoint_plain(code_search_prompt)
                        print("ijjij",refined_response)
                        lines = refined_response.split('\n')
                        last_line = lines[-1].strip()
                        print("nmnmnm",last_line,file_ext)
                        if ("YES" in last_line and similarity>0.741) or ( ( file_name_value!="NA" ) or ( class_value !="NA" ) or ( funcion_value!= "NA" ) ):
                            lines[-1] = f"{code_context}"     
                            print(" 88888888888888888 ",lines[-1]) 
                            refined_response= '\n'.join(lines)
                        else:
                            lines.pop()  
                            refined_response= '\n'.join(lines)
                      
                    elif no_Df == True:
                        print("khali")
                        code_search_prompt+=f"""
You are an helpful AI Assistant please provide an elaborate answer to the user query to the best of your abilities
User Query: {user_prompt}
"""
                    # backend_response = """
# In Java, the `TypeReference` class is used to capture the generic type information at runtime. It is commonly used when working with libraries or frameworks that require generic type information, such as JSON parsing libraries like Jackson or Gson.
# """     
                        refined_response = completion_endpoint_plain(code_search_prompt)
                        # print(query_data["data"],refined_response)
                    # print(query_data["ch"])
                    logging.info(f"Received new message: ")
                    message = {}

                    message['action'] = 'chat'
                    message['message'] = 'valid link'
                    message['chatId'] = query_data["chatId"]
                    message['progressbar'] = True
                    # await websocket.send_json(message)
                    # await asyncio.sleep(8)
                    # logging.info(f"Received new message: {data} ")
                    # logging.info(f"Received new message w/o chtat print: {data} ")
                    # print(no_Df,"ccccccmj",code_search_prompt)
                    message['action'] = 'chat'
                    message['message'] = refined_response
                    message['chatId'] = query_data["chatId"]
                    message['newvalue'] = "acha"
                    message['progressbar'] = False
                    response_timestamp =  int(time.time() * 1000)
                    message['response_timestamp']= response_timestamp
                    print(response_timestamp)
                    # await asyncio.sleep(5)
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print(f"Elapsed Time: {elapsed_time:.2f} seconds")
                    await websocket.send_json(message)       
                    insert_message(query_data["query_timestamp"], query_data["chatId"], 'https://example.com/avatar.png', "User", user_prompt, query_data["query_timestamp"]) 
                    insert_message(response_timestamp, query_data["chatId"], 'https://example.com/avatar.png', "AI Assistant", refined_response,response_timestamp)
                    
    except Exception:
        pass