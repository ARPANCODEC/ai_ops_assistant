import json
import re
from llm.llm_client import call_llm

def extract_city(user_task):
    """
    Extracts city name from user input using simple patterns.
    """
    patterns = [
        r"weather in ([a-zA-Z ]+)",
        r"temperature in ([a-zA-Z ]+)",
        r"weather for ([a-zA-Z ]+)",
        r"weather at ([a-zA-Z ]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, user_task.lower())
        if match:
            return match.group(1).strip().title()

    return None


def plan_task(user_task):
    """
    Planner Agent:
    Uses LLM for structured planning.
    Falls back to intent + city-aware planning if LLM is unavailable.
    """

    # -----------------------------
    # LLM-based planning
    # -----------------------------
    prompt = f"""
You are a Planner Agent.

Convert the user request into a JSON execution plan.

Rules:
- Output ONLY valid JSON
- No explanations
- Each step must include: step_id, action, tool, parameters

Available tools:
- github_search
- weather_fetch

User request:
{user_task}
"""

    response = call_llm(prompt)

    if response:
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            pass  # fall back safely

    # -----------------------------
    # Fallback planning (intent-aware)
    # -----------------------------
    task_lower = user_task.lower()
    steps = []
    step_id = 1

    # GitHub intent
    if any(k in task_lower for k in ["github", "repo", "repository", "repositories"]):
        steps.append({
            "step_id": step_id,
            "action": "Search popular Python GitHub repositories",
            "tool": "github_search",
            "parameters": {
                "query": "python",
                "limit": 3
            }
        })
        step_id += 1

    # Weather intent
    if any(k in task_lower for k in ["weather", "temperature"]):
        city = extract_city(user_task) or "Delhi"

        steps.append({
            "step_id": step_id,
            "action": f"Fetch current weather for {city}",
            "tool": "weather_fetch",
            "parameters": {
                "city": city
            }
        })

    # Safety net
    if not steps:
        steps.append({
            "step_id": 1,
            "action": "Fetch current weather for Delhi",
            "tool": "weather_fetch",
            "parameters": {
                "city": "Delhi"
            }
        })

    return {"steps": steps}
