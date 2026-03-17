# AI API Integration Assignment

Overview:

This project demonstrates the integration of multiple AI APIs using Python. The goal is to understand how to send prompts to different AI models and receive responses.

APIs Used:

* Groq API
* Cohere API
* Google Gemini API

Technologies Used:

* Python
* dotenv (for environment variables)
* API integration

Project Structure:

* `groq_example.py` – Groq API integration
* `cohere_example.py` – Cohere API integration
* `gemini_example.py` – Gemini API integration
* `.env` – Stores API keys securely

Setup Instructions:

1. Clone or download the project
2. Install required libraries:

   ```
   pip install python-dotenv cohere google-generativeai
   ```
3. Create a `.env` file and add your API keys:

   ```
   GROQ_API_KEY=your_key_here
   COHERE_API_KEY=your_key_here
   GOOGLE_API_KEY=your_key_here
   ```
4. Run any file:

   ```
   python cohere_example.py
   ```

Example Prompts:

* What is Artificial Intelligence?
* Explain the universe
* Name the planets


Conclusion:

This project helped in understanding how to work with real-world AI APIs, handle errors, and integrate multiple services in Python.