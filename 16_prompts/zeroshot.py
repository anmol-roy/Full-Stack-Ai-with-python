from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyAwS55PIhIJZIxRc5V8qxyf-WePzA4jcpE",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """You are a highly intelligent question answering bot and only asnswer math relates question.
You will provide detailed and accurate answers to the questions asked by users.
If you do not know the answer to a question, you will respond with 'I do not know the answer to that question.'
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "can you tell me a joke"
        }
    ]
)

print(response.choices[0].message)