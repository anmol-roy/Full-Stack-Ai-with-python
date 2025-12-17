from openai import OpenAI
import requests
import json
from pydantic import BaseModel, Field
from typing import Optional
import os


client = OpenAI(
    api_key="AIzaSyBhs99vTdOQLOw65tJZJsj-zw_xUE0HtcU",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


# ---------------- SYSTEM PROMPT ----------------
SYSTEM_PROMPT = """
You are an expert AI Assistant designed to solve user queries using a
step-by-step structured reasoning workflow.

You MUST strictly follow the step sequence and JSON format.

-------------------------------------------------
STEPS YOU CAN USE
-------------------------------------------------
START, PLAN, TOOL, OBSERVE, OUTPUT

-------------------------------------------------
IMPORTANT RULES
-------------------------------------------------
- Always output VALID JSON
- Only ONE step per response
- Do NOT skip steps
- PLAN can appear multiple times
- TOOL must be followed by OBSERVE
- OUTPUT must be the final response

-------------------------------------------------
JSON OUTPUT FORMAT
-------------------------------------------------
{
  "step": "START | PLAN | TOOL | OBSERVE | OUTPUT",
  "content": "string",
  "tool": "string",
  "input": "string"
}
You are ONLY allowed to call these tools:
- run_command
- get_weather

DO NOT invent tools like bash, shell, mkdir, etc.

"""
def safe_chat_completion(messages):
    while True:
        try:
            return client.chat.completions.create(
                model="gemini-2.5-flash",
                messages=messages,
                response_format={"type": "json_object"}
            )
        except RateLimitError as e:
            print("⏳ Rate limit hit. Waiting 30 seconds...")
            time.sleep(30)


print("/n/n/n")

# ---------------- OUTPUT SCHEMA ----------------
class MyOutputFormat(BaseModel):
    step: Literal["START", "PLAN", "TOOL", "OBSERVE", "OUTPUT"] = Field(...)
    content: Optional[str] = None
    tool: Optional[str] = None
    input: Optional[str] = None

def run_command(cmd :str):
    result = os.system(cmd)
    return result



def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=%c+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The current weather in {city} is {response.text}"
    return "Weather data unavailable."

available_tools = {
    "get_weather": get_weather,
    "run_command": run_command,
    "bash": run_command  # 🔥 alias
}

# ---------------- AGENT LOOP ----------------
def run_agent():
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    user_query = input("🧑: ")
    messages.append({"role": "user", "content": user_query})

    while True:
        response = safe_chat_completion(messages)(
            model="gemini-2.5-flash",
            messages=messages,
            response_format={"type": "json_object"}
        )

        raw = response.choices[0].message.content
        data = json.loads(raw)

        step = data["step"]
        messages.append({"role": "assistant", "content": raw})

        if step == "START":
            print("🔥", data.get("content"))

        elif step == "PLAN":
            print("🧠", data.get("content"))

        elif step == "TOOL":
            tool_name = data.get("tool")
            tool_input = data.get("input")

            print(f"🛠 {tool_name}({tool_input})")

            result = available_tools[tool_name](tool_input)

            observe = {
                "step": "OBSERVE",
                "tool": tool_name,
                "content": result
            }

            messages.append(
                {"role": "assistant", "content": json.dumps(observe)}
            )

        elif step == "OUTPUT":
            print("🤖", data.get("content"))
            break

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    user_query = input("🧑: ")
    messages.append({"role": "user", "content": user_query})

    while True:
        response = client.chat.completions.parse(
            model="gemini-2.5-flash",
            messages=messages,
            response_format={"type": "json_object"}
        )

        raw = response.choices[0].message.parsed
        data = json.loads(raw)

        step = data["step"]
        messages.append({"role": "assistant", "content": raw})

        if step == "START":
            print("🔥", data["content"])

        elif step == "PLAN":
            print("🧠", data["content"])

        elif step == "TOOL":
            tool_name = data["tool"]
            tool_input = data["input"]
            print(f"🛠 {tool_name}({tool_input})")

            result = available_tools[tool_name](tool_input)

            observe = json.dumps({
                "step": "OBSERVE",
                "tool": tool_name,
                "content": result
            })
            messages.append({"role": "assistant", "content": observe})

        elif step == "OUTPUT":
            print("🤖", data["content"])
            break

        # ---------------- RUN ----------------
# ---------------- RUN ----------------
if __name__ == "__main__":
    run_agent()

