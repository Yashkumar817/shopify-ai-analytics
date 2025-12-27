AI-Powered Shopify Analytics App

Overview

This project is a mini AI-powered analytics system designed to answer natural-language business questions for Shopify stores.
It uses a Rails API gateway and a Python FastAPI AI agent to interpret user questions, perform analytics reasoning, and return business-friendly insights.

The focus of this project is system design, agent reasoning, and API orchestration, not production-level Shopify integration.

⸻

🏗️ Architecture

Client (curl / Postman)
|
v
Rails API (API Gateway)
|
v
Python FastAPI (AI Agent)
|
v
Analytics Logic (Mocked ShopifyQL)

Components

1. Rails API (Backend Gateway)
   • Accepts user questions in natural language
   • Validates input (store_id, question)
   • Forwards requests to Python AI service
   • Returns formatted JSON responses

2. Python AI Service (Agent)
   • Interprets user intent (inventory, sales, etc.)
   • Determines required data
   • Executes analytics logic (mocked)
   • Converts results into business-friendly explanations

⸻

⚙️ Setup Instructions

Prerequisites
• Ruby 4.x
• Rails 8.x
• Python 3.x
• macOS / Linux
• Git

⸻

1️⃣ Run Python AI Service

cd python-ai-service
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
python -m uvicorn app.main:app --reload --port 8000

Expected output:

Uvicorn running on http://127.0.0.1:8000

⸻

2️⃣ Run Rails API

cd rails-api
bundle install
rails s

Expected output:

Listening on http://127.0.0.1:3000

⸻

🤖 Agent Flow Description 1. Receive Question
• Input: store_id, question 2. Intent Classification
• Identify whether the question relates to:
• Inventory
• Sales
• Customers (extensible) 3. Planning
• Decide which data is required (e.g., daily sales, inventory levels) 4. Analytics Execution
• Execute mocked Shopify analytics logic (ShopifyQL-like reasoning) 5. Explanation
• Convert raw numbers into simple business language

⸻

📌 Example:

Question:

“How much inventory should I reorder next week?”

Agent Reasoning:
• Intent → Inventory
• Metric → Daily sales
• Time window → Next 7 days
• Result → Reorder recommendation

⸻

🔌 Sample API Requests & Responses

Endpoint

POST /api/v1/questions

⸻

Request Example

curl -X POST http://localhost:3000/api/v1/questions \
-H "Content-Type: application/json" \
-d '{
"store_id": "demo-store.myshopify.com",
"question": "How much inventory should I reorder next week?"
}'

⸻

Response Example

{
"answer": "You sell around 10 units per day. You should reorder at least 70 units for next week.",
"confidence": "medium"
}

⸻

Another Example

Question

{
"store_id": "demo-store.myshopify.com",
"question": "Which products are likely to go out of stock?"
}

Response

{
"answer": "Some products may go out of stock within a week based on recent sales trends.",
"confidence": "medium"
}


🔐 Shopify Integration (Mocked)

• Shopify OAuth and ShopifyQL execution are mocked
• This is intentional and allowed by the assignment
• Architecture supports plugging in:
• Shopify OAuth
• Shopify Admin API
• ShopifyQL analytics queries

🧪 Tech Stack

• Backend API: Ruby on Rails (API-only)
• AI Service: Python + FastAPI
• Agent Logic: Rule-based (LLM-ready)
• Database: SQLite (default)
• HTTP Client: Faraday

🚀 Future Enhancements

• Shopify OAuth integration
• Real ShopifyQL execution
• LLM (OpenAI / Claude) integration
• Conversation memory
• Analytics dashboard

🏁 Conclusion

This project fulfills the assignment’s goal of building a mini AI-powered Shopify analytics system, focusing on reasoning, architecture, and clarity rather than production polish.

