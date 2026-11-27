import tkinter as tk
from tkinter import ttk

class GameTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Translator")
        self.root.geometry("700x500")
        self.root.configure(bg="#10121c")

        title = tk.Label(
            root,
            text="GAME TRANSLATOR 🇫🇷",
            font=("Segoe UI", 25, "bold"),
            bg="#10121c",
            fg="#9b7cff"
        )
        title.pack(pady=25)

        subtitle = tk.Label(
            root,
            text="REAL-TIME GAME DIALOGUE TRANSLATOR",
            font=("Segoe UI", 10),
            bg="#10121c",
            fg="white"
        )
        subtitle.pack()

        self.status = tk.Label(
            root,
            text="Status: Waiting",
            bg="#10121c",
            fg="#00e5a0",
            font=("Segoe UI", 12)
        )
        self.status.pack(pady=30)

        self.start = ttk.Button(
            root,
            text="START TRANSLATION",
            command=self.start_translation
        )
        self.start.pack(pady=10)

        self.stop = ttk.Button(
            root,
            text="STOP",
            command=self.stop_translation
        )
        self.stop.pack(pady=10)

        self.result = tk.Label(
            root,
            text="Your French translations will appear here.",
            bg="#202438",
            fg="white",
            font=("Segoe UI", 14),
            wraplength=600,
            padx=20,
            pady=30
        )
        self.result.pack(pady=30, padx=30, fill="x")

    def start_translation(self):
        self.status.config(text="Status: Ready to translate")

    def stop_translation(self):
        self.status.config(text="Status: Stopped")


if __name__ == "__main__":
    window = tk.Tk()
    app = GameTranslator(window)
    window.mainloop()
