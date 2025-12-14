from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyAwS55PIhIJZIxRc5V8qxyf-WePzA4jcpE",
    base_url="htpps://generativelanguage.googleapis.com/v1beta2"  # Gemini OpenAI endpoint

)
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "user", "content": "explain how ai works in few words"}
    ]
)
print(response.choices[0].message.content)