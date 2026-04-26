from ai import ask_ai
from openai import OpenAI
from ai import ask_ai

print(ask_ai("test"))

client = OpenAI(api_key="78cf86ce1d4c400d8eed629cf3fbb3f0")

def ask_ai(prompt):
    return "Working fine"
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
