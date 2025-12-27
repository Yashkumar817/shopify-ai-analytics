from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import AnalyticsAgent

app = FastAPI()
agent = AnalyticsAgent()

class QuestionRequest(BaseModel):
    store_id: str
    question: str

@app.post("/ask")
def ask(req: QuestionRequest):
    return agent.handle_question(req.store_id, req.question)
