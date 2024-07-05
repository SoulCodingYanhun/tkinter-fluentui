import tkinter as tk
from tkinter import ttk
from ..core import FluentWidget


class Annotation(FluentWidget):
    def __init__(self, master=None, target=None, text="", **kwargs):
        super().__init__(master, **kwargs)
        self.target = target
        self.text = text
        self.widget = tk.Canvas(master, bg="systemTransparent", highlightthickness=0)
        self._create_annotation()

    def create_widget(self):
        return self.widget

    def _create_annotation(self):
        if not self.target:
            return

        x, y, w, h = self.target.winfo_x(), self.target.winfo_y(), self.target.winfo_width(), self.target.winfo_height()
        self.widget.create_rectangle(x, y, x + w, y + h, outline="red", width=2)
        self.widget.create_text(x + w + 5, y, text=self.text, anchor="w", fill="red")


class Coachmark(FluentWidget):
    def __init__(self, master=None, target=None, text="", **kwargs):
        super().__init__(master, **kwargs)
        self.target = target
        self.text = text
        self.widget = tk.Toplevel(master)
        self.widget.overrideredirect(True)
        self.widget.attributes("-topmost", True)
        self.widget.attributes("-alpha", 0.9)
        self._create_coachmark()

    def create_widget(self):
        return self.widget

    def _create_coachmark(self):
        if not self.target:
            return

        x, y, w, h = self.target.winfo_rootx(), self.target.winfo_rooty(), self.target.winfo_width(), self.target.winfo_height()

        self.widget.geometry(f"+{x + w // 2}+{y + h + 10}")

        frame = ttk.Frame(self.widget, style="Fluent.TFrame")
        frame.pack(padx=10, pady=10)

        ttk.Label(frame, text=self.text, style="Fluent.TLabel", wraplength=200).pack()

        ttk.Button(frame, text="Got it", style="Fluent.TButton", command=self.widget.destroy).pack(pady=(10, 0))

    def show(self):
        self.widget.deiconify()

    def hide(self):
        self.widget.withdraw()
