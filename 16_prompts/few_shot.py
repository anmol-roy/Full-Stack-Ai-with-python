from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyAwS55PIhIJZIxRc5V8qxyf-WePzA4jcpE",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# few shot examples
SYSTEM_PROMPT = """You are a highly intelligent question answering bot and only asnswer math relates question.
You will provide detailed and accurate answers to the questions asked by users.
If you do not know the answer to a question, you will respond with 'I do not know the answer to that question.'
rule:
- strictly flow output in json format
output format:
{
  "question": "<repeat the question here>",
  "answer": "<detailed answer here>"
}
examples:
Q, can you help me to solve a + b where a = 2 and b = 3 ?
A, {
    "question": "can you help me to solve a + b where a = 2 and b = 3 ?",
    "answer": "To solve a + b where a = 2 and b = 3, we simply add the two values together. So, 2 + 3 equals 5."
}

Q, what is the derivative of x^2 ?
A, {
    "question": "what is the derivative of x^2 ?",
    "answer": "The derivative of x^2 with respect to x is 2x. This is found using the power rule of differentiation, which states that the derivative of x^n is n*x^(n-1)."
}


"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "van you help me to solve a + b where a = 2 and b = 3 ?"
        }
    ]
)

print(response.choices[0].message)