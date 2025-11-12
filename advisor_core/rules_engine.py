from dataclasses import dataclass
from typing import List, Optional

DEFAULT_REDUCTION_STEP = 10.0  # percent points


@dataclass
class BudgetItem:
    name: str
    current_percent: float
    target_percent: Optional[float] = None
    fixed: bool = False


@dataclass
class Advice:
    item: str
    action: str
    from_percent: Optional[float] = None
    to_percent: Optional[float] = None
    reason: Optional[str] = None


@dataclass
class AdvicePlan:
    headline: str
    advice: List[Advice]


def compute_advice_plan(items: List[BudgetItem]) -> AdvicePlan:
    advice_list: List[Advice] = []

    for item in items:
        if item.fixed:
            advice_list.append(
                Advice(
                    item=item.name,
                    action="explain_fixed",
                    reason=f"{item.name} is a fixed cost and should not be adjusted.",
                )
            )
            continue

        target = item.target_percent
        if target is None and item.current_percent is not None:
            target = max(item.current_percent - DEFAULT_REDUCTION_STEP, 0.0)

        if target is not None and item.current_percent > target:
            advice_list.append(
                Advice(
                    item=item.name,
                    action="reduce_percent",
                    from_percent=item.current_percent,
                    to_percent=target,
                    reason=f"Reduce {item.name} to align with target allocation.",
                )
            )

    headline = "Personalized budget adjustments to align with targets"
    return AdvicePlan(headline=headline, advice=advice_list)


if __name__ == "__main__":
    sample_items = [
        BudgetItem(name="Food", current_percent=50.0, target_percent=35.0),
        BudgetItem(name="Groceries", current_percent=20.0, target_percent=15.0),
        BudgetItem(name="Tuition", current_percent=25.0, fixed=True),
        BudgetItem(name="Travel", current_percent=12.0),
    ]
    plan = compute_advice_plan(sample_items)
    print(plan)

