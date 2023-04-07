import tkinter as tk

class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Control-v>", self.paste_event)

    def paste_event(self, event):
        self.after(10, self.paste)
