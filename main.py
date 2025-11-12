# main.py
import os
from dotenv import load_dotenv
from groq import Groq
import gradio as gr

# Load .env (expects GROQ_API_KEY=sk-...)
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise RuntimeError("Missing GROQ_API_KEY. Put it in .env or export it in your environment.")

client = Groq(api_key=API_KEY)
MODEL = "llama-3.3-70b-versatile"  # change if you want a different model

def build_messages_from_history(history, user_message):
    """
    Convert Gradio chat history (list of [user, bot]) into the `messages` list expected by Groq,
    and append the new user turn.
    """
    messages = []
    # history: list of (user_text, bot_text)
    for user_text, bot_text in history:
        messages.append({"role": "user", "content": user_text})
        messages.append({"role": "assistant", "content": bot_text})
    # add current user message
    messages.append({"role": "user", "content": user_message})
    return messages

def respond(user_message, history):
    """
    Called when user submits a message.
    Returns: updated history and clears the input box (so gr clears it).
    """
    # ensure history is a list; gradio sometimes gives None initially
    if history is None:
        history = []

    # Append a temporary user entry to the history (bot reply will replace the second item)
    # but we'll actually call API then append assistant response.
    messages = build_messages_from_history(history, user_message)

    # Call Groq chat completions
    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=MODEL,
            # you can add other params like max_tokens or temperature here if supported
        )
        assistant_content = chat_completion.choices[0].message.content
    except Exception as e:
        # On error, return an error message in the chat (and keep history)
        assistant_content = f"Error contacting Groq API: {e}"

    # Append the final user+assistant pair to history
    history.append([user_message, assistant_content])
    return history, ""  # second return clears the input box

def reset_chat():
    return []

# Build Gradio UI
with gr.Blocks(title="Groq Chat (Gradio)") as demo:
    gr.Markdown("## Groq Chat — powered by `llama-3.3-70b-versatile`")
    chatbot = gr.Chatbot(label="Chat with model", height=500)
    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Type your message and press Enter", lines=2)
        send = gr.Button("Send")
    with gr.Row():
        clear_btn = gr.Button("Clear")

    # Wire events
    send.click(fn=respond, inputs=[txt, chatbot], outputs=[chatbot, txt])
    txt.submit(fn=respond, inputs=[txt, chatbot], outputs=[chatbot, txt])
    clear_btn.click(fn=reset_chat, inputs=None, outputs=[chatbot])

if __name__ == "__main__":
    demo.launch()