import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your frontend origin
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)
# Configure CORS

messages = []

# Configure logging format
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

@app.get("/")
def root():
    if messages:
        return {"message": messages[-1]}
    else:
        return {"message": "No messages yet"}

@app.get("/api/messages")
def get_messages():
    return {"messages": messages}


@app.post("/api/messages")
def add_message(message: dict):
    new_message = message.get("message")
    print("fdgdfgfdf fgfhf")
    logging.info(f"Received new message: {new_message}")
    messages.append(new_message)
    return {"message": new_message}
