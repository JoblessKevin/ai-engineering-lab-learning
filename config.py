import os

from dotenv import load_dotenv

# 從專案根目錄的 .env 載入環境變數；已存在的系統環境變數不會被覆蓋
load_dotenv()


def get_api_key(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"{name} 尚未設定，請在 .env 中填入")
    return value


GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
