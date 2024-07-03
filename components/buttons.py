import tkinter as tk
from tkinter import ttk
from .core.base import FluentComponent
from .core.styles import apply_theme, COLORS, FONT_SIZES
from .utils.helpers import generate_id

class Button(FluentComponent):
    def __init__(self, master=None, text="", style="primary", size="medium", icon=None, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.text = text
        self.style = style
        self.size = size
        self.icon = icon
        self.command = command
        self.button = None
        self._create_button()

    def _create_button(self):
        self.button = ttk.Button(self.master, text=self.text, command=self.command)
        self._apply_style()
        self._set_icon()
        self.button.pack()

    def _apply_style(self):
        theme = self._get_current_theme()
        button_style = f"Fluent.TButton.{self.style}.{self.size}"
        ttk.Style().configure(button_style,
            background=theme['colors'][self.style],
            foreground=theme['colors']['text_on_' + self.style],
            font=(theme['fonts']['primary'], FONT_SIZES[self.size]),
            padding=(10, 5),
            relief='flat',
            borderwidth=0
        )
        self.button.configure(style=button_style)

    def _set_icon(self):
        if self.icon:
            # Assume we have an IconManager class to handle icons
            icon = IconManager.get_icon(self.icon, size=FONT_SIZES[self.size])
            self.button.configure(image=icon, compound=tk.LEFT)

    def _get_current_theme(self):
        # This should be implemented to get the current theme
        pass

class LinkButton(Button):
    def __init__(self, master=None, text="", url="", **kwargs):
        super().__init__(master, text=text, style="link", **kwargs)
        self.url = url
        self.button.configure(command=self._open_url)

    def _open_url(self):
        import webbrowser
        webbrowser.open(self.url)

class IconButton(Button):
    def __init__(self, master=None, icon=None, **kwargs):
        super().__init__(master, text="", icon=icon, **kwargs)

    def _create_button(self):
        self.button = ttk.Button(self.master, command=self.command)
        self._apply_style()
        self._set_icon()
        self.button.pack()

class ToggleButton(Button):
    def __init__(self, master=None, **kwargs):
        self.is_toggled = False
        super().__init__(master, **kwargs)

    def _create_button(self):
        self.button = ttk.Checkbutton(self.master, text=self.text, command=self._toggle)
        self._apply_style()
        self._set_icon()
        self.button.pack()

    def _toggle(self):
        self.is_toggled = not self.is_toggled
        self._apply_style()
        if self.command:
            self.command(self.is_toggled)

    def _apply_style(self):
        super()._apply_style()
        if self.is_toggled:
            self.button.state(['selected'])
        else:
            self.button.state(['!selected'])

# Factory function to create different types of buttons
def create_button(button_type, *args, **kwargs):
    button_classes = {
        'default': Button,
        'link': LinkButton,
        'icon': IconButton,
        'toggle': ToggleButton
    }
    return button_classes[button_type](*args, **kwargs)
