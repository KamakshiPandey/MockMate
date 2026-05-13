from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Debug check
if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY is missing. Check your .env file.")

# Initialize client
client = Groq(api_key=GROQ_API_KEY)
print("API KEY:", os.getenv("GROQ_API_KEY"))


def ask_ai_question(prompt: str) -> str:
    try:
        print("📤 Sending request to Groq...")
        
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a professional interviewer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        print("✅ Success")

        return response.choices[0].message.content.strip()

    except Exception as e:
        import traceback
        print("❌ FULL ERROR BELOW:")
        traceback.print_exc()   # 👈 THIS LINE IS KEY
        return f"Error: {str(e)}"