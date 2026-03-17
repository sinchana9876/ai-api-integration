import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def query_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    user_input = input("Enter prompt: ")
    print("\nGenerating response...\n")
    result = query_gemini(user_input)
    print("\nResponse:\n")
    print(result)