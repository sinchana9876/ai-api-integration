import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-base"
headers = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"
}

def query_hf(prompt):
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        
        print("DEBUG:", response.text)   # 👈 VERY IMPORTANT (to see real error)

        data = response.json()

        if isinstance(data, list):
            return data[0].get("generated_text", "No response")
        elif isinstance(data, dict):
            return data.get("error", str(data))
        else:
            return "Unexpected response format"

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    user_input = input("Enter prompt: ")
    print("\nGenerating response...\n")
    result = query_hf(user_input)
    print("\nResponse:\n")
    print(result)