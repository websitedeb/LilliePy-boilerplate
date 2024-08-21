from os import getenv

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def use_ai(prompt):
  client = OpenAI()
  client.api_key = str(getenv("KEY"))
  completion = client.chat.completions.create(model="gpt-4o",
                                              messages=[{
                                                  "role": "user",
                                                  "content": f"{prompt}"
                                              }])
  return completion
