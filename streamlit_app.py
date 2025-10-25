import json
from openai import OpenAI

client = OpenAI(
    api_key = "YOUR_API_KEY_GOES_HERE_IM_NOT_SHARING_MINE"
)

# 1
system_prompt = """
You are a type writer. You start off with an empty string. Whenever a user gives you a word, you add
it to the string. Always return back what the string looks like.
"""

# 2
chat_history = [
    {"role": "system", "content": system_prompt},
]

# 3
while True:
    user_prompt = input("What do you want to ask? ")
    
    # 4
    chat_history.append(
        {"role": "user", "content": user_prompt},
    )
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages = chat_history
    )

    assistant_response = response.choices[0].message.content
    print(assistant_response)
    print()

    # 5
    chat_history.append(
        {"role": "assistant", "content": assistant_response}
    )
