from typing import Dict, List

from advisor_core.advisor_voice import generate_message_with_llama3
from advisor_core.rules_engine import BudgetItem, AdvicePlan, compute_advice_plan


def build_items_from_snapshot(snapshot: Dict[str, float]) -> List[BudgetItem]:
    targets = {"Food": 35.0, "Groceries": 15.0}
    fixed_flags = {"Tuition": True}

    items: List[BudgetItem] = []
    for name, current in snapshot.items():
        items.append(
            BudgetItem(
                name=name,
                current_percent=float(current),
                target_percent=targets.get(name),
                fixed=fixed_flags.get(name, False),
            )
        )
    return items


def build_advice_and_message(snapshot: Dict[str, float]) -> (AdvicePlan, str):
    items = build_items_from_snapshot(snapshot)
    plan = compute_advice_plan(items)
    message = generate_message_with_llama3(plan)
    return plan, message


if __name__ == "__main__":
    snapshot_data = {"Food": 50.0, "Groceries": 20.0, "Tuition": 25.0}
    plan, message = build_advice_and_message(snapshot_data)
    print(plan)
    print()
    print(message)

