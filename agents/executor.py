from tools.github_tool import github_search
from tools.weather_tool import weather_fetch

def execute_plan(plan):
    """
    Executor Agent:
    Executes each planned step using tools.
    """
    outputs = []

    for step in plan["steps"]:
        tool = step["tool"]
        params = step["parameters"]

        if tool == "github_search":
            result = github_search(**params)
        elif tool == "weather_fetch":
            result = weather_fetch(**params)
        else:
            result = {"error": "Unknown tool"}

        outputs.append({
            "step_id": step["step_id"],
            "action": step["action"],
            "result": result
        })

    return outputs
