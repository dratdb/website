import openai
import tkinter as tk
from tkinter import scrolledtext, END

# Set up the OpenAI API key
openai.api_key = ""

# Set up the initial prompt to start the conversation
prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."

# Create the main application window
root = tk.Tk()
root.title("GPT-3 Chatbot")

# Create the chat display box
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
chat_display.pack()

# Create the input box and send button
input_box = tk.Entry(root, width=50)
input_box.pack()

def send_message():
    # Get the user's message from the input box
    user_input = input_box.get()

    # Send the user's message to the OpenAI API and get a response
    response = openai.Completion.create(
        engine="davinci",
        prompt=(prompt + "\nUser: " + user_input + "\nAI:"),
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Get the response message from the API and display it in the chat display box
    message = response.choices[0].text.strip()
    chat_display.insert(END, "You: " + user_input + "\n")
    chat_display.insert(END, "Bot: " + message + "\n\n")

    # Clear the input box
    input_box.delete(0, END)

# Create the send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Start the Tkinter main loop
root.mainloop()
