from google import genai
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("GOOGLE_API_KEY not found")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Call Gemini
response = client.models.generate_content(
    model="models/gemini-flash-latest",
    contents="Say hello in one short sentence."
)

print(response.text)
