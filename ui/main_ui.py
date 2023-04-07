import tkinter as tk
from .ui_elements import (
    create_text_input,
    create_output_label,
    create_output_entry,
    create_browse_button,
    create_language_label,
    create_language_menu,
    create_download_button,
)

def create_ui(app, output_folder, language, browse_output_folder, process_phrases, on_ctrl_enter):
    from .styles import apply_styles

    apply_styles()

    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)

    text_input = create_text_input(app)
    create_output_label(app)
    create_output_entry(app, output_folder)
    create_browse_button(app, browse_output_folder)
    create_language_label(app)
    create_language_menu(app, language, ["English", "Spanish"])
    create_download_button(app, process_phrases)

    return text_input
