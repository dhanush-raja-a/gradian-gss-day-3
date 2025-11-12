🧠 Groq Chat — Gradio App

A lightweight Gradio chat interface powered by the Groq API and the llama-3.3-70b-versatile model.
Deployed free on Hugging Face Spaces.

🔗 Live Demo: https://huggingface.co/spaces/DhanushRajaA/groq-chat￼

⸻

🚀 Features
• Interactive chat UI built with Gradio Blocks
• Uses Groq LLM API for real-time responses
• Simple, clean design — ready to extend

⸻

⚙️ Setup (Local)

git clone <repo-url>
cd groq-chat
pip install -r requirements.txt
echo "GROQ_API_KEY=sk-xxxx" > .env
python app.py

Then open: http://127.0.0.1:7860

⸻

☁️ Deploy on Hugging Face Spaces 1. Create a new Space → choose Gradio SDK 2. Push your files (app.py, requirements.txt, etc.) 3. Add your GROQ_API_KEY under Settings → Secrets

The Space builds automatically — no server setup needed.

⸻

🧩 Requirements

gradio>=3.0
groq
python-dotenv
pydantic>=2.10.6,<2.11

⸻

🪪 Author

Dhanush Raja A
Jr. AIML Engineer
