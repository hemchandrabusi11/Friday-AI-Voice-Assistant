import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

conversation_history = [
    {"role": "system", "content": "You are Friday, a calm, sharp, helpful AI assistant similar to the AI from Iron Man. Keep replies short, natural, and conversational for voice output."}
]

def think(query):
    conversation_history.append({"role": "user", "content": query})
    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=conversation_history,
            max_tokens=150,
            extra_headers={
                "HTTP-Referer": "https://neuraflowy.com",
                "X-Title": "Friday AI Assistant"
            }
        )
        reply = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        return f"I'm having trouble thinking right now: {e}"