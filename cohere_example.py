import os
import cohere
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def query_cohere(prompt):
    try:
        response = co.chat(
            message=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    user_input = input("Enter prompt: ")
    print("\nGenerating response...\n")
    result = query_cohere(user_input)
    print("\nResponse:\n")
    print(result)