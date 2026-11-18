
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

prompt = """
Give exactly 5 healthy breakfast ideas.

Rules:
- Number from 1 to 5.
- One line per idea.
- No introduction or conclusion.
- Include protein, fibre and healthy fats.
- Include Indian and international options.
"""

reply = llm.invoke(prompt)

print(reply.content)