from tkinter import ttk

def apply_styles():
    style = ttk.Style()

    style.configure("TLabel", font=("Helvetica", 12))
    style.configure("TEntry", font=("Helvetica", 12))
    style.configure("TButton", font=("Helvetica", 12), padding=5)
    style.configure("TOptionMenu", font=("Helvetica", 12), padding=5)

    # Configure the style of the Text widget
    style.configure("Text", font=("Helvetica", 12))
    style.map("Text", background=[("active", "#f0f0f0"), ("!disabled", "#f0f0f0")])
