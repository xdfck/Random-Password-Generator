import tkinter as tk
import customtkinter as ctk
import random
import string
import json
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class PasswordGenerator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Random Password Generator")
        self.geometry("500x600")
        self.history_file = "history.json"
        self.history = self.load_history()

        # UI Элементы
        self.label = ctk.CTkLabel(self, text="Password Generator", font=("Arial", 24, "bold"))
        self.label.pack(pady=20)

        # Ползунок длины
        self.length_label = ctk.CTkLabel(self, text=f"Длина: 12")
        self.length_label.pack()
        self.slider = ctk.CTkSlider(self, from_=4, to_=32, command=self.update_slider_label)
        self.slider.set(12)
        self.slider.pack(pady=10)

        # Чекбоксы
        self.use_letters = ctk.CTkCheckBox(self, text="Буквы (a-z, A-Z)")
        self.use_letters.select()
        self.use_letters.pack(pady=5)

        self.use_numbers = ctk.CTkCheckBox(self, text="Цифры (0-9)")
        self.use_numbers.select()
        self.use_numbers.pack(pady=5)

        self.use_symbols = ctk.CTkCheckBox(self, text="Спецсимволы (!@#$)")
        self.use_symbols.pack(pady=5)

        # Кнопка генерации
        self.gen_button = ctk.CTkButton(self, text="Сгенерировать", command=self.generate_password)
        self.gen_button.pack(pady=20)

        # Поле для результата
        self.result_entry = ctk.CTkEntry(self, width=300, justify="center")
        self.result_entry.pack(pady=10)

        # Таблица (список) истории
        self.history_list = tk.Listbox(self, bg="#2b2b2b", fg="white", borderwidth=0, highlightthickness=0)
        self.history_list.pack(pady=10, fill="both", expand=True, padx=20)
        self.refresh_history_ui()

    def update_slider_label(self, value):
        self.length_label.configure(text=f"Длина: {int(value)}")

    def generate_password(self):
        length = int(self.slider.get())
        chars = ""
        if self.use_letters.get(): chars += string.ascii_letters
        if self.use_numbers.get(): chars += string.digits
        if self.use_symbols.get(): chars += string.punctuation

        if not chars:
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, "Выберите параметры!")
            return

        password = "".join(random.choice(chars) for _ in range(length))
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, password)
        
        self.save_to_history(password)

    def save_to_history(self, pwd):
        self.history.insert(0, pwd)
        self.history = self.history[:10]  # Храним последние 10
        with open(self.history_file, "潮流", encoding="utf-8") as f:
            json.dump(self.history, f)
        self.refresh_history_ui()

    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as f:
                return json.load(f)
        return []

    def refresh_history_ui(self):
        self.history_list.delete(0, tk.END)
        for item in self.history:
            self.history_list.insert(tk.END, item)

if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()
