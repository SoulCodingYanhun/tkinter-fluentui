import tkinter as tk
from tkinter import ttk
from ..core.base import FluentComponent
from ..core.styles import FluentUIStyles, FluentUIColors

class FluentProgressBar(FluentComponent):
    def __init__(self, master=None, mode='determinate', value=0, maximum=100, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.mode = mode
        self.value = value
        self.maximum = maximum
        self.progress_bar = None
        self._create_widget()

    def _create_widget(self):
        style = ttk.Style()
        style.configure(
            'Fluent.Horizontal.TProgressbar',
            troughcolor=FluentUIColors.BACKGROUND_NEUTRAL_LIGHTER,
            background=FluentUIColors.ACCENT,
            thickness=4  # Adjust thickness for a sleeker look
        )

        self.progress_bar = ttk.Progressbar(
            self.master,
            orient='horizontal',
            mode=self.mode,
            maximum=self.maximum,
            value=self.value,
            style='Fluent.Horizontal.TProgressbar'
        )

        if self.id:
            self.progress_bar.configure(id=self.id)
        if self.className:
            self.progress_bar.configure(class_=self.className)

    def render(self):
        self.progress_bar.pack(pady=10, padx=10, fill=tk.X)
        return self.progress_bar

    def set_value(self, value):
        self.value = value
        self.progress_bar['value'] = value

    def get_value(self):
        return self.progress_bar['value']

    def set_mode(self, mode):
        self.mode = mode
        self.progress_bar['mode'] = mode

class FluentSpinner(FluentComponent):
    def __init__(self, master=None, size=30, speed=50, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.size = size
        self.speed = speed
        self.canvas = None
        self.spinner = None
        self._create_widget()

    def _create_widget(self):
        self.canvas = tk.Canvas(self.master, width=self.size, height=self.size, 
                                bg=FluentUIColors.BACKGROUND_LIGHT, highlightthickness=0)
        
        # Create arc for spinner
        start = 0
        extent = 60
        self.spinner = self.canvas.create_arc(4, 4, self.size-4, self.size-4, 
                                              start=start, extent=extent, width=4,
                                              style=tk.ARC, outline=FluentUIColors.ACCENT)

        if self.id:
            self.canvas.configure(id=self.id)
        if self.className:
            self.canvas.configure(class_=self.className)

    def render(self):
        self.canvas.pack(pady=10, padx=10)
        self._animate()
        return self.canvas

    def _animate(self):
        angle = int(self.canvas.itemcget(self.spinner, 'start'))
        new_angle = (angle + 10) % 360
        self.canvas.itemconfigure(self.spinner, start=new_angle)
        self.master.after(self.speed, self._animate)

    def start(self):
        self._animate()

    def stop(self):
        self.master.after_cancel(self._animate)

class FluentLoadingBar(FluentComponent):
    def __init__(self, master=None, width=200, height=4, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.width = width
        self.height = height
        self.canvas = None
        self.bar = None
        self._create_widget()

    def _create_widget(self):
        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height, 
                                bg=FluentUIColors.BACKGROUND_NEUTRAL_LIGHTER, highlightthickness=0)
        
        # Create initial bar
        self.bar = self.canvas.create_rectangle(0, 0, 0, self.height, 
                                                fill=FluentUIColors.ACCENT, width=0)

        if self.id:
            self.canvas.configure(id=self.id)
        if self.className:
            self.canvas.configure(class_=self.className)

    def render(self):
        self.canvas.pack(pady=10, padx=10)
        self._animate()
        return self.canvas

    def _animate(self):
        width = self.canvas.winfo_width()
        x = self.canvas.coords(self.bar)[0]
        if x < width:
            self.canvas.coords(self.bar, x, 0, x + 50, self.height)
            self.canvas.move(self.bar, 3, 0)
        else:
            self.canvas.coords(self.bar, -50, 0, 0, self.height)
        self.master.after(20, self._animate)

    def start(self):
        self._animate()

    def stop(self):
        self.master.after_cancel(self._animate)

# Assumed content of FluentUIStyles and FluentUIColors (you would define these in core/styles.py)
class FluentUIStyles:
    TYPOGRAPHY = {
        'body': {'fontFamily': 'Segoe UI', 'fontSize': 14},
    }

class FluentUIColors:
    BACKGROUND_LIGHT = '#FFFFFF'
    BACKGROUND_NEUTRAL_LIGHTER = '#F3F2F1'
    ACCENT = '#0078D4'
