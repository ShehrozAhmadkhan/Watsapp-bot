from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

entry = 5
history = [
    {"role": "user", "content": "University mein attendance policy kya hai?"},
    {"role": "assistant", "content": "Attendance 75% required hai."}
]

def add_to_history(history,u_q,a_a):
    history.append({"role":"user","content":u_q})
    history.append({"role":"assistant","content":a_a})

    limit = entry*2
    if len(history) > limit:
        history = history[-limit:]
    return history


new_user_question = "Aghr is sa kum ho jay?"

prompt = f""" You are a helping assistant and your goal is to create a reformulated query!
this is the history : {history}
and this is the new user question : {new_user_question}
just give me a reformulated query nothing else and only query!"""

llm = client.chat.completions.create(model="gpt-4o-mini",messages=[{"role":"user","content":prompt}])
reformulated_query = llm.choices[0].message.content
print(reformulated_query)