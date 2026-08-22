import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("api_key_nemo")

if not API_KEY:
    raise ValueError(
        "api_key_nemo not found in .env"
    )

MODEL = "nvidia/nemotron-3-ultra-550b-a55b"

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=API_KEY
)