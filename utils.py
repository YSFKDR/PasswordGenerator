# utils.py
def copy_to_clipboard(window, text):
    window.clipboard_clear()
    window.clipboard_append(text)
