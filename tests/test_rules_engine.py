from advisor_core.rules_engine import (
    Advice,
    AdvicePlan,
    BudgetItem,
    compute_advice_plan,
)


def advice_to_tuple(advice: Advice):
    return (
        advice.item,
        advice.action,
        advice.from_percent,
        advice.to_percent,
    )


def test_known_targets_respected():
    items = [
        BudgetItem(name="Food", current_percent=50.0, target_percent=35.0),
        BudgetItem(name="Tuition", current_percent=20.0, fixed=True),
    ]
    plan = compute_advice_plan(items)

    assert isinstance(plan, AdvicePlan)
    advice_pairs = {advice_to_tuple(a) for a in plan.advice} # line of code uses a set comprehension in Python.
    assert ("Food", "reduce_percent", 50.0, 35.0) in advice_pairs
    assert any(a.action == "explain_fixed" for a in plan.advice)


def test_unknown_category_uses_default_reduction():
    items = [BudgetItem(name="Travel", current_percent=22.0)]
    plan = compute_advice_plan(items)

    assert len(plan.advice) == 1
    advice = plan.advice[0]
    assert advice.item == "Travel"
    assert advice.action == "reduce_percent"
    assert advice.to_percent == 12.0

