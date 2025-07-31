import os
import requests
from dotenv import load_dotenv
from langchain_groq.chat_models import ChatGroq

load_dotenv()


def get_models() -> list[str]:
    try:
        api_key = os.environ.get("GROQ_API_KEY")
        url = os.environ.get("MODELS_URL")

        if not api_key or not url:
            raise EnvironmentError(
                "Missing GROQ_API_KEY or MODELS_URL in environment variables."
            )

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json().get("data", [])
        models = [
            d["id"] for d in data if "whisper" not in d["id"] and "tts" not in d["id"]
        ]
        return sorted(models)  # Sort the list for consistent order

    except Exception as e:
        print(f"[Error] {e}")
        return []


def get_response(model: str, history: list, max_hist: int = 3):
    chat = ChatGroq(model=model)
    for chunk in chat.stream(history[-2 * max_hist :]):
        yield chunk.content
