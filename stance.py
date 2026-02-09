import os
import re
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Allowed outputs
VALID_STANCES = {"positive", "negative", "neutral", "mixed"}

def get_entity_stance(sentence: str, entity: str) -> str:
    """
    Returns the stance toward an entity in a sentence.
    Output is strictly one of:
    positive | negative | neutral | mixed
    """

    prompt = f"""
You are a stance classification engine.

Task:
Determine the stance expressed toward the given ENTITY in the given SENTENCE.

Definitions:
- positive: clearly favorable opinion toward the entity
- negative: clearly unfavorable opinion toward the entity
- neutral: factual or no sentiment toward the entity
- mixed: both positive and negative sentiment toward the entity

Rules:
- Respond with ONLY ONE WORD.
- Allowed outputs: positive, negative, neutral, mixed
- Use lowercase only.
- No punctuation.
- No explanation.

ENTITY: "{entity}"
SENTENCE: "{sentence}"
"""

    try:
        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=prompt,
        )

        # Read model output
        raw_output = response.text.strip().lower()

        # Clean unexpected characters
        cleaned = re.sub(r"[^a-z]", "", raw_output)

        # Validate output
        if cleaned in VALID_STANCES:
            return cleaned
        else:
            return "neutral"

    except Exception:
        # Any error → safe fallback
        return "neutral"
