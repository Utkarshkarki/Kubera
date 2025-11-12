from typing import Any, Dict, List, Text

import datetime

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionLogExpense(Action):
    def name(self) -> Text:
        return "action_log_expense"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[Dict[Text, Any]]:
        amount = tracker.get_slot("amount")
        category = tracker.get_slot("category")
        subcategory = tracker.get_slot("subcategory")
        date_str = tracker.get_slot("date")

        try:
            amount_value = float(str(amount).replace(",", "").strip())
        except Exception:
            amount_value = None

        if not date_str or str(date_str).lower() in {"today", "now"}:
            date_iso = datetime.date.today().isoformat()
        elif str(date_str).lower() == "yesterday":
            date_iso = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
        else:
            date_iso = str(date_str)

        expense_record = {
            "amount": amount_value,
            "category": category,
            "subcategory": subcategory,
            "date": date_iso,
        }
        # TODO: persist expense_record to your datastore

        return []

