from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyAwS55PIhIJZIxRc5V8qxyf-WePzA4jcpE",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "you are an ecpert in maths and only ans maths related questions. if the question is not related to maths, respond with 'i can only answer maths related questions'."},
        {
            "role": "user",
            "content": "van you help me to solve a + b where a = 2 and b = 3 ?"
        }
    ]
)

print(response.choices[0].message)