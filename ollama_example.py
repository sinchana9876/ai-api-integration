import requests

def query_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt}
        )
        return response.json()["response"]
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print(query_ollama(input("Enter prompt: ")))