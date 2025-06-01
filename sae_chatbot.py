import tkinter as tk
from tkinter import ttk, scrolledtext
from nltk.chat.util import Chat, reflections
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

voice_options = {voice.name: voice.id for voice in voices}

pairs = [
    [r"(.*)my name is (.*)", ["Ok and %2?"]],
    [r"(.*)help(.*)", ["I don't care~"]],
    [r"(.*) your name\??", ["My name is Sae'yang."]],
    [r"how are you(.*)\?", ["I'm doing my best TT", "I am great!"]],
    [r"sorry(.*)", ["You are not forgiven", "It's OK, I mind", "You should be"]],
    [r"I'm (.*) (good|well|okay|ok)", ["And why do I care?", "Great! Moving on"]],
    [r"(hi|hey|hola|hello|holla)(.*)", ["Hm", "."]],
    [r"what (.*) want\??", ["To love Chu Si"]],
    [r"(.*)created(.*)\??", ["Wouldn't you like to know?", "Top secret ;)"]],
    [r"(.*)(location|city)\??", ["Milky Way"]],
    [r"how (.*) health (.*)", ["Does it matter? But you only die once"]],
    [r"who is (.*)\?", ["Shouldn't you know?"]],
    [r"quit", ["Thank God. Leave quicker next time", "I hope there won't be a next time"]],
    [r"(.*)", ["Hmm. Couldn't care less, don't you have work to do?"]],
]

chat = Chat(pairs, reflections)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_area.insert(tk.END, "You: " + user_input + "\n")
    entry.delete(0, tk.END)

    response = chat.respond(user_input)
    chat_area.insert(tk.END, "Sae'yang: " + response + "\n")
    speak(response)

    if user_input.lower() == "quit":
        root.quit()

def change_voice(event=None):
    selected_voice_name = voice_selector.get()
    selected_voice_id = voice_options[selected_voice_name]
    engine.setProperty('voice', selected_voice_id)

def change_theme(event=None):
    theme = theme_selector.get()
    if theme == "Dark":
        chat_area.config(bg="#1e1e1e", fg="#ffffff", insertbackground="#ffffff")
        entry.config(bg="#2e2e2e", fg="#ffffff", insertbackground="#ffffff")
        send_button.config(bg="#3a3a3a", fg="#ffffff")
        root.config(bg="#121212")
    else:
        chat_area.config(bg="#ffffff", fg="#000000", insertbackground="#000000")
        entry.config(bg="#f0f0f0", fg="#000000", insertbackground="#000000")
        send_button.config(bg="#C6F6FF", fg="#000000")
        root.config(bg="#ffffff")

root = tk.Tk()
root.title("Sae'yang - Chatbot 💬🎤")
root.geometry("600x550")

top_frame = tk.Frame(root)
top_frame.pack(pady=10)

theme_label = tk.Label(top_frame, text="Theme:")
theme_label.pack(side=tk.LEFT, padx=5)

theme_selector = ttk.Combobox(top_frame, values=["Light", "Dark"])
theme_selector.current(0)
theme_selector.pack(side=tk.LEFT)
theme_selector.bind("<<ComboboxSelected>>", change_theme)

voice_label = tk.Label(top_frame, text="Voice:")
voice_label.pack(side=tk.LEFT, padx=10)

voice_selector = ttk.Combobox(top_frame, values=list(voice_options.keys()), width=30)
voice_selector.current(0)
voice_selector.pack(side=tk.LEFT)
voice_selector.bind("<<ComboboxSelected>>", change_voice)

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, font=("Arial", 12))
chat_area.pack(padx=10, pady=10)
chat_area.insert(tk.END, "Sae'yang: Hi, I'm Sae'yang. Type 'quit' to leave.\n")
chat_area.config(state=tk.NORMAL)

entry_frame = tk.Frame(root)
entry_frame.pack(pady=5)

entry = tk.Entry(entry_frame, width=50, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=(0, 10))
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(entry_frame, text="Send", command=send_message, font=("Arial", 12), bg="#C6F6FF")
send_button.pack(side=tk.LEFT)

change_voice()
change_theme()

root.mainloop()
