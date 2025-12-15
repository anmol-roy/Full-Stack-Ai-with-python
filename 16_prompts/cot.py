from openai import OpenAI
import json

client = OpenAI(
    api_key="AIzaSyAwS55PIhIJZIxRc5V8qxyf-WePzA4jcpE",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
You are a math-only assistant.

Rules:
- Answer ONLY math-related questions.
- Respond in VALID JSON only.
- Run ONLY ONE step at a time.
- If step is "plan", output must be null.
- If step is "output", plan must be null.

JSON format:
{
  "step": "<plan | output>",
  "plan": "<high-level plan or null>",
  "output": "<final answer or null>"
}
"""

question = "solve a + b where a = 2 and b = 3"

# -------- STEP 1 : PLAN --------
response_plan = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
        {"role": "assistant", "content": '{"step":"plan","plan":null,"output":null}'}
    ]
)

# plan_json = json.loads(response_plan.choices[0].message.content)

# print("PLAN STEP:")
# print(json.dumps(plan_json, indent=2))

