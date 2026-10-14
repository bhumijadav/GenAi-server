
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(
    title="GenAI Application",
    description="A simple GenAI chatbot API",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str
    timestamp: str


@app.get("/")
def home():
    return {
        "message": "Welcome to the GenAI Application!",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "GenAI"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    user_message = request.message.strip()

    if not user_message:
        reply = "Please enter a message."
    else:
        reply = (
            f"You asked: {user_message}. "
            "This is a demo response. "
            "Connect an AI model to generate intelligent answers."
        )

    return ChatResponse(
        reply=reply,
        timestamp=datetime.now().isoformat()
    )
