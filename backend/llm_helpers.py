# Import OpenAI client class from the new openai>=1.0.0 SDK
from openai import OpenAI

# Standard library imports
import os
from dotenv import load_dotenv

# Load environment variables from a .env file, if present
load_dotenv()

# Instantiate the OpenAI client using the API key from environment variables
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text: str) -> str:
    """
    Summarizes the input text (usually a GitHub README) using OpenAI's GPT model.

    Args:
        text (str): The input text to be summarized (e.g., README content).

    Returns:
        str: A summarized version of the input text, or an error message if something fails.
    """
    try:
        # Call OpenAI Chat Completion API with user/system messages
        response = client.chat.completions.create(
            model="gpt-4",  # Use GPT-4 model
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that summarizes GitHub repositories based on their README files."
                },
                {
                    "role": "user",
                    "content": f"Summarize this GitHub repository based on its README:\n\n{text}"
                }
            ],
            max_tokens=300,   # Limit summary size
            temperature=0.5   # Moderate randomness for more consistent output
        )

        # Return the model's response (trimmed of leading/trailing whitespace)
        return response.choices[0].message.content.strip()

    except Exception as e:
        # Return a fallback message if the API call fails
        return f"OpenAI API error: {e}"
