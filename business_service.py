from fastapi import FastAPI
import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


@app.get("/")
def root():
    return {"description": "Business Logic Service for data processing with LLM call"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/process")
def process_data(payload: dict):
    if OPENROUTER_API_KEY:
        # Static prompt for LLM
        prompt = "What are LeBron James career points? Return just the number."
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }
        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}]
        }

        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=10
            )
            result = response.json()
            message = result.get("choices", [{}])[0].get("message", {}).get("content", "No response")

            return {
                "question": prompt,
                "llm_response": message
            }

        except Exception as e:
            return {"error": "LLM call failed", "details": str(e)}
    else:
        # Fallback: simulate processing
        time.sleep(2)
        return {"original": payload, "processed": True}