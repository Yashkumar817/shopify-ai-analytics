def classify_intent(question):
    q = question.lower()
    if "inventory" in q or "reorder" in q:
        return "inventory"
    if "top" in q or "selling" in q:
        return "sales"
    return "unknown"

def explain_result(intent, data):
    if intent == "inventory":
        return (
            f"You sell around {data['daily_sales']} units per day. "
            f"You should reorder at least {data['daily_sales'] * 7} units for next week."
        )
    if intent == "sales":
        return "These are your top selling products from last week."
    return "Not enough data to answer clearly."
