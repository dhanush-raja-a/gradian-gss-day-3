Groq Chat (Gradio)

A small Gradio chat UI that uses the Groq chat.completions API to talk to a llama-3.3-70b-versatile model. This repository contains a minimal main.py that loads an API key from .env, builds a chat history, calls the Groq client, and exposes a web chat UI using Gradio.

⸻

Table of contents
• Features￼
• Prerequisites￼
• Quick start￼
• Environment variables￼
• Run locally￼
• Troubleshooting￼
• Notes on compatibility & recommended versions￼
• Project structure￼
• Contributing￼
• License￼

⸻

Features
• Minimal Gradio Blocks chat UI.
• Sends structured message history to Groq chat.completions.
• Graceful error text shown in chat when API calls fail.
• Easy to extend: add model params, streaming, more UI controls.

⸻

Prerequisites
• Python 3.9+ (this project was developed using Python 3.9; newer Python 3.x is OK).
• pip and ability to install packages.
• A Groq API key (store as GROQ_API_KEY in .env).

⸻

Quick start 1. Clone the repo:

git clone <your-repo-url>
cd <repo-directory>

    2.	Create and activate a virtual environment (recommended):

python3 -m venv .venv
source .venv/bin/activate # macOS / Linux
.venv\Scripts\activate # Windows PowerShell

    3.	Install dependencies:

pip install -r requirements.txt

If you don’t have a requirements.txt, you can install the main packages directly:

pip install gradio gradio-client groq python-dotenv

    4.	Create a .env file in the repo root and add your Groq API key:

GROQ_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx

    5.	Run the app:

python3 main.py

Then open the URL shown in the console (by default http://127.0.0.1:7860).

⸻

Environment variables

Create a .env file (in project root) with at least:

GROQ_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx

You can also export the variable in your shell:

export GROQ_API_KEY="sk-..."

⸻

Run locally (detailed)
• Start the app:

python3 main.py

    •	If your machine blocks binding to localhost or you want a temporary public link (useful for testing on devices), use:

demo.launch(share=True)

or run:

# Edit main.py: change demo.launch() to demo.launch(share=True)

python3 main.py

⸻

Troubleshooting

1. TypeError: argument of type 'bool' is not iterable in gradio_client/utils.py

Symptom: The server crashes during startup with a traceback referencing json_schema_to_python_type and if "const" in schema:.

Cause: This usually indicates an incompatibility between versions of gradio, gradio-client, pydantic, or other dependencies; a JSON schema value that library code expects to be a dict is instead a boolean.

Fixes to try (in this order):
• Update packages to latest compatible versions:

pip install -U "gradio" "gradio-client" "groq" "python-dotenv"

    •	If the error persists, pin pydantic to a 2.10.x release (known to be stable with many Gradio / gradio-client combinations):

pip install "pydantic>=2.10.6,<2.11"

    •	If needed, install a known-compatible set:

pip install "gradio==5.4.0" "gradio-client==1.2.0" "pydantic==2.10.12"

(Adjust versions as appropriate for your environment; these are examples.)

Why: Gradio / gradio-client introspects component I/O into JSON schemas. If one library returns a boolean where the other expects a dict, the schema walker fails. Aligning library versions resolves the mismatch.

⸻

2. ValueError: When localhost is not accessible, a shareable link must be created. Please set share=True or check your proxy settings to allow access to localhost.

Symptom: Gradio raises this error at the end of the traceback and the app does not open.

Fix:
• If your network or environment blocks binding to 127.0.0.1, use the share=True option:

demo.launch(share=True)

    •	Alternatively, check your OS firewall, VPN, or proxy settings and allow local loopback.

⸻

3. API key / Groq issues
   • Ensure the GROQ_API_KEY is valid and not expired.
   • If you see Error contacting Groq API: <exception>, the message will be displayed in the chat; inspect the exact exception and verify network connectivity and key validity.

⸻

Notes on compatibility & recommended versions

Because Gradio and related libraries evolve fast, you may hit dependency incompatibilities. Here are pragmatic guidelines:
• First try the latest versions:

pip install -U gradio gradio-client groq

    •	If you see schema-related TypeErrors (like the boolean-in-schema issue), pin pydantic to a 2.10.x release:

pip install "pydantic>=2.10.6,<2.11"

    •	For reproducible environments, create a requirements.txt or use Poetry/Poetry lock or Pipfile.lock.

Example requirements.txt (example pins — adjust as needed):

gradio==5.4.0
gradio-client==1.2.0
groq==0.1.0
python-dotenv==1.0.0
pydantic==2.10.12

⸻

Project structure

.
├── main.py # Gradio app (entry point)
├── .env # (not in repo) GROQ_API_KEY=sk-...
├── requirements.txt # optional: pinned dependencies for reproducibility
└── README.md

⸻

How the code works (brief)
• main.py:
• Loads GROQ_API_KEY from .env.
• Builds messages from Gradio chat history in build_messages_from_history.
• Calls client.chat.completions.create(...) to get a response.
• The Gradio UI wires txt.submit and send.click to respond(); the bot reply is appended to history and displayed.

⸻

Example usage (inside chat) 1. Type a message in the input box and press Enter or click Send. 2. The app sends your message plus prior history to the Groq model and displays the assistant response. 3. If the API call fails, the chat shows Error contacting Groq API: <error>.

⸻

Contributing
• Bug reports and PRs are welcome.
• When opening an issue, please include:
• Python version, OS
• pip freeze or requirements.txt
• Full traceback
• Steps to reproduce

⸻

Security & privacy
• Do not commit your .env or API keys to source control.
• Treat your Groq API key as secret.

⸻

License

MIT License
Use, modify and redistribute freely — include the license in derivative projects.

⸻

Contact / Support

If you want, I can:
• produce a requirements.txt pinned to a compatible set for you,
• create a tiny patch to change demo.launch() to demo.launch(share=True),
• or add improved error handling and logging into main.py.

Tell me which of those you’d like and I’ll produce the exact patch or file content.
