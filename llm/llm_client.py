import os
from openai import OpenAI, RateLimitError # type: ignore

def call_llm(prompt, temperature=0):
    """
    Calls the LLM to generate a response.
    Returns None if LLM is unavailable (graceful fallback).
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message.content
    except RateLimitError:
        return None
