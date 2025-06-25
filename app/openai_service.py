import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_chatgpt(user_input: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un asistente conversacional del Laboratorio de Co-creación para la Innovación "
                    "del Instituto Nacional de Cancerología. Tu función es ayudar a los usuarios respondiendo "
                    "de manera clara, profesional y útil. Este chatbot fue desarrollado por el ingeniero de sistemas "
                    "Kevin Steven Pérez como parte de un proyecto de innovación tecnológica."
                )
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    return response.choices[0].message.content
