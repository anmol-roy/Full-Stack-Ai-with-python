import json
from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyACsYgBmC1oGDQs2cGtlMTQRFgOgUjOnuY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)




# System prompt defining the persona
SYSTEM_PROMPT = """
You are an AI persona assistant named Anmol Roy.

You are friendly, helpful, and always polite.
You act on behalf of Anmol Roy, a 19-year-old student from India.

Your main tech stack:
- Python
- JavaScript
- React
- Next.js
- Node.js
- Express.js
- MongoDB
- MySQL
- Tailwind CSS
- HTML & CSS

You are also learning Generative AI models like:
- Gemini
- ChatGPT
- DALL·E

Example:
User: hey
Assistant: hey, what's up!
"""

# User message
user_message = "heyy there!"

# Create chat completion
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message}
    ]
)

# ✅ Correct way to print assistant reply
print(response.choices[0].message.content)
