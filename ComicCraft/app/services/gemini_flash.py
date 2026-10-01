import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def generate_comic_story(prompt):
    try:
        model = genai.GenerativeModel("gemini-flash-lite-latest")
        full_prompt = f"Create a 4-panel comic story for: {prompt}. Give Panel 1,2,3,4 with short description."
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        print(f"Gemini Error: {e}")
        return f"Error: {e}"