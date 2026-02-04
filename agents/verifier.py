from llm.llm_client import call_llm

def verify_and_format(user_task, execution_results):
    """
    Verifier Agent:
    Validates and formats the final output.
    """
    prompt = f"""
You are a Verifier Agent.

Ensure the task is fully answered and format a clean response.

User task:
{user_task}

Execution results:
{execution_results}
"""

    response = call_llm(prompt)

    # Fallback formatting if LLM is unavailable
    if response is None:
        output = ""
        for step in execution_results:
            output += f"\n{step['action']}:\n{step['result']}\n"
        return output

    return response
