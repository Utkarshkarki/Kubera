import http.client
import json
from typing import List

from advisor_core.rules_engine import AdvicePlan


def plan_to_text_instructions(plan: AdvicePlan) -> str:
    lines: List[str] = [plan.headline, ""]
    for advice in plan.advice:
        if (
            advice.action == "reduce_percent"
            and advice.from_percent is not None
            and advice.to_percent is not None
        ):
            lines.append(
                f"- Cut {advice.item} from {advice.from_percent:.0f}% to {advice.to_percent:.0f}%."
            )
        elif advice.action == "explain_fixed":
            lines.append(f"- {advice.item} is a fixed cost.")
        else:
            lines.append(f"- {advice.item}: {advice.reason or advice.action}.")
    return "\n".join(lines)


def generate_message_with_llama3(plan: AdvicePlan) -> str:
    instructions = plan_to_text_instructions(plan)
    system_prompt = (
        "You are a friendly financial advisor chatbot. "
        "Use clear, supportive language. Never invent numbers; "
        "only explain and humanize the provided plan."
    )
    user_prompt = (
        "Please write a helpful message for the user based on these instructions:\n"
        f"{instructions}\n"
        "Explain briefly what to change and why, and keep it concise."
    )

    conn = http.client.HTTPConnection("localhost", 11434)
    payload = {
        "model": "llama3:8b",
        "system": system_prompt,
        "prompt": user_prompt,
        "stream": False,
        "options": {"temperature": 0.6},
    }
    conn.request(
        "POST",
        "/api/generate",
        body=json.dumps(payload),
        headers={"Content-Type": "application/json"},
    )
    response = conn.getresponse()
    data = json.loads(response.read().decode("utf-8"))
    conn.close()
    return data.get("response", "").strip()


if __name__ == "__main__":
    from advisor_core.rules_engine import BudgetItem, compute_advice_plan

    items = [
        BudgetItem(name="Food", current_percent=50.0, target_percent=35.0),
        BudgetItem(name="Groceries", current_percent=20.0, target_percent=15.0),
        BudgetItem(name="Tuition", current_percent=25.0, fixed=True),
    ]
    plan = compute_advice_plan(items)
    print(generate_message_with_llama3(plan))

