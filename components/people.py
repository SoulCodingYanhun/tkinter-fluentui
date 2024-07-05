import tkinter as tk
from tkinter import ttk
from ..core import FluentWidget
from PIL import Image, ImageTk


class PersonaGroup(FluentWidget):
    def __init__(self, master=None, personas=None, **kwargs):
        super().__init__(master, **kwargs)
        self.personas = personas or []
        self.widget = ttk.Frame(master)
        self._create_group()

    def create_widget(self):
        return self.widget

    def _create_group(self):
        for i, persona in enumerate(self.personas):
            frame = ttk.Frame(self.widget)
            frame.pack(side=tk.LEFT, padx=(0 if i == 0 else -10, 0))

            if 'image' in persona:
                img = Image.open(persona['image'])
                img = img.resize((32, 32), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(img)
                label = ttk.Label(frame, image=photo)
                label.image = photo  # keep a reference
            else:
                label = ttk.Label(frame, text=persona['name'][0],
                                  style="PersonaInitial.TLabel")
            label.pack()

    def add_persona(self, persona):
        self.personas.append(persona)
        self._create_group()  # Recreate the entire group


class PersonCard(FluentWidget):
    def __init__(self, master=None, name="", job_title="", email="", image=None, **kwargs):
        super().__init__(master, **kwargs)
        self.name = name
        self.job_title = job_title
        self.email = email
        self.image = image
        self.widget = ttk.Frame(master, style="PersonCard.TFrame")
        self._create_card()

    def create_widget(self):
        return self.widget

    def _create_card(self):
        if self.image:
            img = Image.open(self.image)
            img = img.resize((64, 64), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            image_label = ttk.Label(self.widget, image=photo)
            image_label.image = photo  # keep a reference
            image_label.pack(side=tk.LEFT, padx=10, pady=10)
        else:
            initial_label = ttk.Label(self.widget, text=self.name[0],
                                      style="PersonCardInitial.TLabel")
            initial_label.pack(side=tk.LEFT, padx=10, pady=10)

        info_frame = ttk.Frame(self.widget)
        info_frame.pack(side=tk.LEFT, padx=10, pady=10)

        name_label = ttk.Label(info_frame, text=self.name, style="PersonCardName.TLabel")
        name_label.pack(anchor=tk.W)

        job_label = ttk.Label(info_frame, text=self.job_title, style="PersonCardJob.TLabel")
        job_label.pack(anchor=tk.W)

        email_label = ttk.Label(info_frame, text=self.email, style="PersonCardEmail.TLabel")
        email_label.pack(anchor=tk.W)
