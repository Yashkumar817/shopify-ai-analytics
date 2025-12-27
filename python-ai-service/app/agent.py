from app.utils import classify_intent, explain_result
from app.shopify_client import ShopifyClient

class AnalyticsAgent:
    def __init__(self):
        self.shopify = ShopifyClient()

    def handle_question(self, store_id, question):
        intent = classify_intent(question)
        query = self.build_shopifyql(intent)
        data = self.shopify.run_query(store_id, query)
        answer = explain_result(intent, data)

        return {
            "answer": answer,
            "confidence": "medium"
        }

    def build_shopifyql(self, intent):
        if intent == "inventory":
            return "SELECT inventory, daily_sales FROM inventory"
        if intent == "sales":
            return "SELECT product, total_sales FROM sales"
        return ""
