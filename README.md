# 🧠 PhiloAgents – AI-Powered Simulation Engine

PhiloAgents is an AI-driven simulation engine that brings historical philosophers to life through dynamic, real-time interactions. This project combines LLMs, agentic architectures, memory systems, and modern Python tools to simulate intelligent conversations with lifelike philosophical agents.

---

## 🚀 What This Project Does

This simulation framework allows you to:

- Interact with intelligent agents representing Plato, Aristotle, and Turing.
- Deploy a real-time API with FastAPI + WebSockets.
- Equip agents with short-term and long-term memory using MongoDB.
- Implement advanced RAG (Retrieval-Augmented Generation) techniques.
- Track, evaluate, and improve agent performance with built-in observability.

---

## 📦 Tech Stack Overview

| Component       | Technology                         |
|----------------|-------------------------------------|
| Backend         | Python, FastAPI, WebSockets         |
| Agent Framework | LangGraph, LangChain                |
| LLM Inference   | GroqCloud, OpenAI (optional)        |
| Memory          | MongoDB                             |
| Dev Tools       | Docker, uv, ruff                    |

---

## 🔧 Core Features

- 🧠 Intelligent agent design with modular LangGraph pipelines  
- 📚 Knowledge retrieval from external sources for RAG  
- 🧵 Long-term and short-term memory support  
- 🎭 Prompt engineering for personality simulation  
- 🌐 REST + WebSocket API interface  
- 📊 Observability and LLMOps practices

---

## 📁 Project Structure

.
├── philoagents-api/ # Core agent logic, APIs, memory, and RAG
└── philoagents-ui/ # Optional frontend interface (Node.js based)

yaml
Copy
Edit

All essential simulation logic is within the `philoagents-api` directory.

---

## 🎮 Philosophers Simulated

| Agent      | Topics Covered                          |
|------------|------------------------------------------|
| Plato      | Metaphysics, justice, forms              |
| Aristotle  | Logic, politics, virtue ethics           |
| Turing     | Computation, AI, consciousness           |

---

## ⚙️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/philoagents.git
cd philoagents-api
2. Set up environment
bash
Copy
Edit
uv venv
source .venv/bin/activate
pip install -r requirements.txt
3. Create .env file
Add your API keys (Groq, OpenAI) in .env.

4. Run the API
bash
Copy
Edit
uvicorn app.main:app --reload
💰 Cost Breakdown
Most features run for free. Only optional evaluation tools require a small API cost:

Service	Estimated Max Cost
Groq API	$0 (Free-tier)
OpenAI API	~$1 (Optional)

🧪 Agent Evaluation & Monitoring
Includes:

LLM-as-a-judge agent evaluation

Prompt version tracking

Real-time debugging and improvement loop

📚 Knowledge Base
Agents use long-term memory populated from:

Wikipedia

Stanford Encyclopedia of Philosophy

No manual downloads needed — handled automatically via backend scripts.

🧰 Dev Practices
Clean, modular Python architecture

Docker-ready

Follows modern best practices (uv, ruff)

Easily extendable for other agents and topics

