from google import genai

client = genai.Client(
    api_key="AIzaSyAwS55PIhIJZIxRc5V8qxyf-WePzA4jcpE"
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="explain how ai works in few words"
)

print(response.text)