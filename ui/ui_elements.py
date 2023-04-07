import tkinter as tk
from tkinter import ttk

from .custom_widgets import CustomText

def create_text_input(app):
    text_input = CustomText(app, wrap="word")
    text_input.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    return text_input


def paste_text(event):
    try:
        event.widget.insert(tk.INSERT, event.widget.clipboard_get())
    except tk.TclError:
        pass
    return "break"


def create_output_label(app):
    output_label = ttk.Label(app, text="Output folder:")
    output_label.grid(row=1, column=0, sticky="w", padx=5)

def create_output_entry(app, output_folder):
    output_entry = ttk.Entry(app, textvariable=output_folder)
    output_entry.grid(row=2, column=0, sticky="ew", padx=5)

def create_browse_button(app, command):
    browse_button = ttk.Button(app, text="Browse", command=command)
    browse_button.grid(row=3, column=0, sticky="ew", padx=5)

def create_language_label(app):
    language_label = ttk.Label(app, text="Select language:")
    language_label.grid(row=4, column=0, sticky="w", padx=5)

def create_language_menu(app, language, language_names):
    language_menu = ttk.OptionMenu(app, language, *language_names)
    language_menu.grid(row=5, column=0, sticky="ew", padx=5)

def create_download_button(app, command):
    download_button = ttk.Button(app, text="Download Sounds", command=command)
    download_button.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
