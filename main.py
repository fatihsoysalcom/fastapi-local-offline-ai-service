from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# This example demonstrates a simple, local 'AI' service using FastAPI.
# It simulates an offline AI component that could be part of a larger
# desktop application (e.g., built with Tauri) for local processing.

app = FastAPI(
    title="Offline AI Coding Studio - Local AI Service",
    description="A simple FastAPI service demonstrating local, offline AI processing."
)

class TextInput(BaseModel):
    text: str

# --- Simulate a simple, rule-based 'AI' function ---
# In a real application, this would be a more complex model (e.g., a Rust/PyO3 module
# or a Python ML library like scikit-learn, transformers) loaded locally.
# For this single-file example, we use a basic keyword-based sentiment analysis.

def analyze_turkish_sentiment(text: str) -> str:
    text_lower = text.lower()
    positive_keywords = ["iyi", "harika", "mükemmel", "güzel", "başarılı"]
    negative_keywords = ["kötü", "berbat", "felaket", "çirkin", "yetersiz"]

    positive_score = sum(1 for keyword in positive_keywords if keyword in text_lower)
    negative_score = sum(1 for keyword in negative_keywords if keyword in text_lower)

    if positive_score > negative_score:
        return "Pozitif"
    elif negative_score > positive_score:
        return "Negatif"
    else:
        return "Nötr"

# --- FastAPI Endpoints ---

@app.get("/", summary="Root endpoint")
async def read_root():
    return {"message": "Welcome to the local AI service! Send text to /analyze_sentiment"}

@app.post("/analyze_sentiment", summary="Analyze text sentiment locally")
async def analyze_sentiment(input_data: TextInput):
    # Call our simulated local AI function
    sentiment = analyze_turkish_sentiment(input_data.text)
    return {"input_text": input_data.text, "sentiment": sentiment, "source": "local_offline_ai"}


if __name__ == "__main__":
    # To run this, you need uvicorn installed: pip install uvicorn
    # The host '127.0.0.1' ensures it's only accessible locally, emphasizing 'local power'.
    uvicorn.run(app, host="127.0.0.1", port=8000)
