AI Operations Assistant (Streamlit)

An AI Operations Assistant that accepts natural-language tasks, plans execution steps using multiple agents, calls real third-party APIs, and produces a complete end-to-end result.

The project runs locally on localhost using Streamlit and demonstrates:

Multi-agent architecture

LLM-based structured reasoning

Real API integrations

One-command local execution

📁 Folder Structure
ai_ops_assistant/                 # Root project directory
│
├── agents/                       # Core multi-agent logic
│   ├── __init__.py               # Marks agents as a Python package
│   ├── planner.py                # Planner Agent: converts user input into execution steps
│   ├── executor.py               # Executor Agent: executes planned steps using tools/APIs
│   └── verifier.py               # Verifier Agent: validates and formats final output
│
├── tools/                        # External tool integrations (real APIs)
│   ├── __init__.py               # Marks tools as a Python package
│   ├── github_tool.py            # Fetches popular GitHub repositories
│   └── weather_tool.py           # Fetches real-time weather data
│
├── llm/                          # LLM abstraction layer
│   ├── __init__.py               # Marks LLM module as a Python package
│   └── llm_client.py             # Handles LLM calls and fallback logic
│
├── main.py                       # Streamlit entry point (runs full agent pipeline)
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variable template
└── README.md                     # Project documentation

🚀 Setup Instructions (Run Locally)
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Configure Environment Variables

Create a .env file from the example:

cp .env.example .env


Update .env with your API keys:

OPENAI_API_KEY=your_openai_api_key
GITHUB_TOKEN=your_github_token
WEATHER_API_KEY=your_openweather_api_key

▶️ Running the Project (One Command)
streamlit run main.py


The application will be available at:

http://localhost:8501

🧠 Architecture Overview

The system follows a multi-agent design:

🧩 Planner Agent

Converts natural-language input into a structured JSON execution plan

Identifies intent (GitHub search, weather query, or both)

Uses an LLM when available

Falls back to rule-based intent planning if the LLM is unavailable

⚙️ Executor Agent

Executes each step in the plan

Calls real third-party APIs

Returns structured results

✅ Verifier Agent

Validates task completion

Formats the final response

Ensures end-to-end correctness

🛠️ Tools

Tools are isolated from agents

Each tool wraps a real external API

No responses are hard-coded

🌐 Integrated APIs
API	Purpose
GitHub Search API	Fetch popular Python repositories
OpenWeather API	Fetch real-time weather data

All data returned by the system is live and real, not mocked.

🧪 Test Cases (Use These to Verify the System)
🌦️ Weather-Only

Tell me today’s weather in Bangalore

What is the current weather in Mumbai?

How is the weather in New York right now?

What’s the temperature in London?

🐙 GitHub-Only

Show popular Python GitHub repositories

Find top Python repositories on GitHub

List trending Python projects from GitHub

🔀 Combined (GitHub + Weather)

Find popular Python GitHub repositories and tell me the weather in Mumbai

Show trending Python projects and today’s weather in Bangalore

⚠️ Known Limitations / Trade-offs

Tool support is limited to implemented APIs

No caching of API responses

Sequential execution (no parallel calls)

LLM quota limits may trigger fallback mode
