import tkinter as tk
from tkinter import ttk
from ..core import FluentWidget


class Dialog(tk.Toplevel, FluentWidget):
    def __init__(self, parent, title=None, **kwargs):
        tk.Toplevel.__init__(self, parent, **kwargs)
        FluentWidget.__init__(self, parent, **kwargs)

        self.transient(parent)
        if title:
            self.title(title)
        self.parent = parent
        self.result = None

        body = ttk.Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        self.buttonbox()

        self.grab_set()
        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.geometry("+%d+%d" % (parent.winfo_rootx() + 50,
                                  parent.winfo_rooty() + 50))
        self.initial_focus.focus_set()
        self.wait_window(self)

    def body(self, master):
        content = ttk.Frame(master)
        content.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        ttk.Label(content, text="Enter your name:").pack()
        self.entry = ttk.Entry(content)
        self.entry.pack(pady=10)

        return self.entry  # Initial focus

    def buttonbox(self):
        box = ttk.Frame(self)

        ok_button = ttk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE)
        ok_button.pack(side=tk.LEFT, padx=5, pady=5)
        cancel_button = ttk.Button(box, text="Cancel", width=10, command=self.cancel)
        cancel_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    def ok(self, event=None):
        if not self.validate():
            self.initial_focus.focus_set()
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()
        self.cancel()

    def cancel(self, event=None):
        self.parent.focus_set()
        self.destroy()

    def validate(self):
        return len(self.entry.get().strip()) > 0

    def apply(self):
        self.result = self.entry.get().strip()


class Modal(Dialog):
    def __init__(self, parent, title=None, message=None, **kwargs):
        self.message = message
        super().__init__(parent, title, **kwargs)

    def body(self, master):
        content = ttk.Frame(master)
        content.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        if self.message:
            ttk.Label(content, text=self.message, wraplength=300).pack(pady=10)

        return content  # No specific initial focus

    def buttonbox(self):
        box = ttk.Frame(self)

        ok_button = ttk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE)
        ok_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.ok)

        box.pack()

    def validate(self):
        return True  # Always valid as it's just an informational modal

    def apply(self):
        self.result = True  # Indicate that the modal was acknowledged