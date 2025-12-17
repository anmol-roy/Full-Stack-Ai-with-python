from openai import OpenAI
import requests



client = OpenAI(
    api_key="AIzaSyBhs99vTdOQLOw65tJZJsj-zw_xUE0HtcU",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%c+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The current weather in {city} is: {response.text}"
    else:
        return "Could not retrieve weather data."


def main():
    user_query = input("Enter your weather query: ")
    response =  client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            
            {"role": "user", "content": user_query},
        ],
    )

    print(f"🤖: {response.choices[0].message.content} ")

print(get_weather("delhi"))