# gui.py
import tkinter as tk
from tkinter import messagebox
from password_generator import generate_password
from utils import copy_to_clipboard

def run_app():
    previous_password = [""]

    def generate():
        length = length_slider.get()
        include_letters = letters_var.get()
        include_mixed = mixed_case_var.get()
        include_punctuation = punctuation_var.get()
        include_numbers = numbers_var.get()

        new_password = generate_password(length, include_letters, include_mixed, include_punctuation, include_numbers, previous_password[0])
        if new_password:
            password_entry.delete(0, tk.END)
            password_entry.insert(0, new_password)
            previous_password[0] = new_password
        else:
            messagebox.showerror("Error", "Please select at least one character set")

    def copy():
        copy_to_clipboard(window, password_entry.get())

    def update_length_label(value):
        length_label.config(text=f"Password Length (4-64): {value}")

    def toggle_theme():
        current_theme = theme_label.cget('text')
        if current_theme == 'Dark':
            apply_light_theme()
            theme_label.config(text='Light', bg="#2e2e2e", fg="white")
        else:
            apply_dark_theme()
            theme_label.config(text='Dark', bg="#f0f0f0", fg="black")

    def apply_dark_theme():
        window.config(bg="#2e2e2e")
        title_label.config(bg="#2e2e2e", fg="white")
        length_label.config(bg="#2e2e2e", fg="white")
        password_frame.config(bg="#3b3b3b")
        password_entry.config(bg="#3b3b3b", fg="white")
        slider_frame.config(bg="#3b3b3b")
        length_slider.config(bg="#3b3b3b", fg="white", troughcolor="#3b3b3b")
        options_frame.config(bg="#2e2e2e")
        letters_check.config(bg="#2e2e2e", fg="white", selectcolor="#3b3b3b")
        mixed_case_check.config(bg="#2e2e2e", fg="white", selectcolor="#3b3b3b")
        punctuation_check.config(bg="#2e2e2e", fg="white", selectcolor="#3b3b3b")
        numbers_check.config(bg="#2e2e2e", fg="white", selectcolor="#3b3b3b")
        theme_label.config(bg="#f0f0f0", fg="black")

    def apply_light_theme():
        window.config(bg="#f0f0f0")
        title_label.config(bg="#f0f0f0", fg="black")
        length_label.config(bg="#f0f0f0", fg="black")
        password_frame.config(bg="#ffffff")
        password_entry.config(bg="#ffffff", fg="black")
        slider_frame.config(bg="#ffffff")
        length_slider.config(bg="#ffffff", fg="black", troughcolor="#e0e0e0")
        options_frame.config(bg="#f0f0f0")
        letters_check.config(bg="#f0f0f0", fg="black", selectcolor="#ffffff")
        mixed_case_check.config(bg="#f0f0f0", fg="black", selectcolor="#ffffff")
        punctuation_check.config(bg="#f0f0f0", fg="black", selectcolor="#ffffff")
        numbers_check.config(bg="#f0f0f0", fg="black", selectcolor="#ffffff")
        theme_label.config(bg="#2e2e2e", fg="white")

    # Setting up the main window
    window = tk.Tk()
    window.title("Password Generator")
    window.geometry("500x500")

    # Define the font style
    font_style = ("Lato", 12)
    title_font_style = ("Lato", 16, "bold")
    theme_font_style = ("Lato", 10)

    # Title
    title_label = tk.Label(window, text="Generate your password", font=title_font_style)
    title_label.pack(pady=20)

    # Theme toggle label
    theme_label = tk.Label(window, text="Dark", font=theme_font_style, bg="#2e2e2e", fg="white", cursor="hand2")
    theme_label.place(relx=1.0, x=-30, y=10, anchor="ne")
    theme_label.bind("<Button-1>", lambda e: toggle_theme())

    # Password display area
    password_frame = tk.Frame(window, bd=2, relief="groove")
    password_frame.pack(pady=10, padx=20, fill="x")

    password_entry = tk.Entry(password_frame, font=font_style, width=30, bd=0, highlightthickness=0)
    password_entry.pack(padx=10, pady=10, fill="x")

    # Password length slider
    length_label = tk.Label(window, text="Password Length (4-64): 12", font=font_style)
    length_label.pack(pady=10)

    slider_frame = tk.Frame(window, bd=2, relief="groove")
    slider_frame.pack(padx=20, fill="x")

    length_slider = tk.Scale(slider_frame, from_=4, to_=64, orient=tk.HORIZONTAL, font=font_style, command=update_length_label, showvalue=0, highlightthickness=0, borderwidth=0)
    length_slider.set(12)
    length_slider.pack(padx=10, pady=5, fill="x")

    # Checkboxes for options
    options_frame = tk.Frame(window)
    options_frame.pack(pady=10)

    letters_var = tk.BooleanVar(value=True)
    mixed_case_var = tk.BooleanVar(value=True)
    punctuation_var = tk.BooleanVar(value=True)
    numbers_var = tk.BooleanVar(value=True)

    letters_check = tk.Checkbutton(options_frame, text="Letters", variable=letters_var, font=font_style)
    letters_check.grid(row=0, column=0, sticky="w")
    mixed_case_check = tk.Checkbutton(options_frame, text="Mixed case", variable=mixed_case_var, font=font_style)
    mixed_case_check.grid(row=1, column=0, sticky="w")
    punctuation_check = tk.Checkbutton(options_frame, text="Punctuation", variable=punctuation_var, font=font_style)
    punctuation_check.grid(row=2, column=0, sticky="w")
    numbers_check = tk.Checkbutton(options_frame, text="Numbers", variable=numbers_var, font=font_style)
    numbers_check.grid(row=3, column=0, sticky="w")

    # Generate and copy buttons
    generate_button = tk.Button(window, text="Generate Password", command=generate, font=font_style, bg="#4CAF50", fg="white", activebackground="#45a049", width=20, bd=0, padx=10, pady=10)
    generate_button.pack(pady=10)
    copy_button = tk.Button(window, text="Copy Password", command=copy, font=font_style, bg="#008CBA", fg="white", activebackground="#007bb5", width=20, bd=0, padx=10, pady=10)
    copy_button.pack(pady=10)

    # Apply initial dark theme
    apply_dark_theme()

    # Run the application
    window.mainloop()
