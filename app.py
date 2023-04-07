import os
import tkinter as tk
from tkinter import filedialog
from sound_downloader import download_sound
from ui.main_ui import create_ui

# rest of the code


CONFIG_FILE = "config.txt"

def save_config():
    with open(CONFIG_FILE, "w") as f:
        f.write(output_folder.get())

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return f.read().strip()
    return ""

def browse_output_folder():
    output_folder.set(filedialog.askdirectory())
    save_config()

def process_phrases(event=None):
    phrases = text_input.get("1.0", tk.END).strip().split("\n")
    destination_folder = output_folder.get()
    selected_language = language_codes[language_names.index(language.get())]

    if not destination_folder:
        print("Please select an output folder.")
        return

    for phrase in phrases:
        download_sound(phrase, selected_language, destination_folder)

    text_input.delete("1.0", tk.END)  # Clear the text input field

def on_ctrl_enter(event):
    process_phrases()

app = tk.Tk()
app.title("Sound Downloader")

output_folder = tk.StringVar()
language = tk.StringVar(app)

language_names = ["English", "Spanish"]
language_codes = ["en-US", "es-ES"]

language.set(language_names[0])  # default value

text_input = create_ui(app, output_folder, language, browse_output_folder, process_phrases, on_ctrl_enter)

app.bind("<Control-Return>", on_ctrl_enter)

output_folder.set(load_config())  # Load the last saved output folder

app.mainloop()
