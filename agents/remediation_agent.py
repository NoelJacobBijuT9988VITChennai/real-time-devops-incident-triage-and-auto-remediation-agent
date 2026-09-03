"""
LLM-based Remediation Planner
"""

import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def create_plan(root_cause, runbook):

    prompt = f"""
    Root Cause:
    {root_cause}

    Runbook:
    {runbook}

    Generate:

    1. Recommended Action
    2. Risk Level
    3. Explanation
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content