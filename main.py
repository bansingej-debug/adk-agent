from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Request(BaseModel):
    message: str

def run_agent(user_input: str) -> str:
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi Janvi! 👋 How can I help you?"
    elif "career" in user_input:
        return "Focus on AI, coding, and internships!"
    else:
        return "I'm your AI agent 😊"

@app.get("/")
def home():
    return {"message": "Agent is running 🚀"}

@app.post("/chat")
def chat(req: Request):
    return {"response": run_agent(req.message)}