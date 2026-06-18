from fastapi import APIRouter
from pydantic import BaseModel
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

router = APIRouter()

# Store conversation history for the current session
conversation_history = []


class ChatRequest(BaseModel):
    message: str


@router.post("/course/chat")
def course_chat(request: ChatRequest):
    global conversation_history

    conversation_history.append({
        "role": "user",
        "parts": [request.message]
    })

    system_prompt = """
You are an AI Course Planning Assistant.

Your job is to help mentors create structured courses.

If information is missing, ask for:
- Subject
- Target audience
- Duration
- Learning goals

Once enough information is available, generate ONLY valid JSON in this format:

{
  "title": "",
  "target_audience": "",
  "duration": "",
  "learning_goals": [],
  "modules": [
    {
      "title": "",
      "objectives": [],
      "lessons": [],
      "resources": [],
      "assessment": ""
    }
  ]
}

Support follow-up modifications naturally.
"""

    chat = model.start_chat(history=[])

    response = chat.send_message(
        system_prompt + "\n\nConversation:\n" +
        "\n".join(
            msg["parts"][0]
            for msg in conversation_history
        )
    )

    conversation_history.append({
        "role": "model",
        "parts": [response.text]
    })

    return {
        "response": response.text
    }