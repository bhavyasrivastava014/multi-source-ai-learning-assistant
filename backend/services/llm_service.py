import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_llm(context, question):
    prompt = f"""
You are an AI Learning Assistant.

Use ONLY the provided context to answer.

If the answer is not found in the context, respond exactly:

"I couldn't find this information in the uploaded material."

Provide concise, well-formatted answers using bullet points whenever appropriate.

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(prompt)

    return response.text
