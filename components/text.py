import tkinter as tk
from tkinter import ttk, font
from ..core.base import FluentComponent
from ..core.styles import FluentUIStyles, FluentUIColors

class FluentLabel(FluentComponent):
    def __init__(self, master=None, text="", variant="body", color=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.text = text
        self.variant = variant
        self.color = color or FluentUIColors.TEXT_PRIMARY
        self.label = None
        self._create_widget()

    def _create_widget(self):
        style = ttk.Style()
        font_specs = FluentUIStyles.TYPOGRAPHY.get(self.variant, FluentUIStyles.TYPOGRAPHY['body'])
        
        style.configure(
            f'Fluent.TLabel.{self.variant}',
            font=(font_specs['fontFamily'], font_specs['fontSize'], font_specs['fontWeight']),
            foreground=self.color,
            padding=font_specs.get('padding', (0, 0, 0, 0))
        )

        self.label = ttk.Label(
            self.master,
            text=self.text,
            style=f'Fluent.TLabel.{self.variant}'
        )

        if self.id:
            self.label.configure(id=self.id)
        if self.className:
            self.label.configure(class_=self.className)

    def render(self):
        self.label.pack(pady=5, padx=5, anchor='w')
        return self.label

    def update_text(self, new_text):
        self.text = new_text
        self.label.configure(text=self.text)

    def update_variant(self, new_variant):
        self.variant = new_variant
        font_specs = FluentUIStyles.TYPOGRAPHY.get(self.variant, FluentUIStyles.TYPOGRAPHY['body'])
        self.label.configure(
            style=f'Fluent.TLabel.{self.variant}',
            font=(font_specs['fontFamily'], font_specs['fontSize'], font_specs['fontWeight'])
        )

class FluentText(FluentComponent):
    def __init__(self, master=None, content="", multiline=False, width=None, height=None, readonly=False, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.content = content
        self.multiline = multiline
        self.width = width
        self.height = height
        self.readonly = readonly
        self.text_widget = None
        self._create_widget()

    def _create_widget(self):
        style = ttk.Style()
        font_specs = FluentUIStyles.TYPOGRAPHY['body']
        
        style.configure(
            'Fluent.TEntry',
            font=(font_specs['fontFamily'], font_specs['fontSize']),
            foreground=FluentUIColors.TEXT_PRIMARY,
            background=FluentUIColors.BACKGROUND_LIGHT,
            bordercolor=FluentUIColors.BORDER,
            relief='flat',
            padding=5
        )

        if self.multiline:
            self.text_widget = tk.Text(
                self.master,
                wrap=tk.WORD,
                width=self.width,
                height=self.height,
                font=(font_specs['fontFamily'], font_specs['fontSize']),
                foreground=FluentUIColors.TEXT_PRIMARY,
                background=FluentUIColors.BACKGROUND_LIGHT,
                relief='flat',
                padx=5,
                pady=5
            )
            self.text_widget.insert(tk.END, self.content)
            if self.readonly:
                self.text_widget.configure(state='disabled')
        else:
            self.text_widget = ttk.Entry(
                self.master,
                width=self.width,
                style='Fluent.TEntry'
            )
            self.text_widget.insert(0, self.content)
            if self.readonly:
                self.text_widget.configure(state='readonly')

        if self.id:
            self.text_widget.configure(id=self.id)
        if self.className:
            self.text_widget.configure(class_=self.className)

    def render(self):
        self.text_widget.pack(pady=5, padx=5, fill=tk.X, expand=True)
        return self.text_widget

    def get_content(self):
        if isinstance(self.text_widget, tk.Text):
            return self.text_widget.get("1.0", tk.END).strip()
        else:
            return self.text_widget.get()

    def set_content(self, new_content):
        if isinstance(self.text_widget, tk.Text):
            self.text_widget.delete("1.0", tk.END)
            self.text_widget.insert(tk.END, new_content)
        else:
            self.text_widget.delete(0, tk.END)
            self.text_widget.insert(0, new_content)

    def set_readonly(self, readonly):
        self.readonly = readonly
        if isinstance(self.text_widget, tk.Text):
            self.text_widget.configure(state='disabled' if readonly else 'normal')
        else:
            self.text_widget.configure(state='readonly' if readonly else 'normal')

# Assumed content of FluentUIStyles and FluentUIColors (you would define these in core/styles.py)
class FluentUIStyles:
    TYPOGRAPHY = {
        'header': {'fontFamily': 'Segoe UI', 'fontSize': 28, 'fontWeight': 'bold', 'padding': (0, 0, 10, 0)},
        'subheader': {'fontFamily': 'Segoe UI', 'fontSize': 20, 'fontWeight': 'normal', 'padding': (0, 0, 8, 0)},
        'body': {'fontFamily': 'Segoe UI', 'fontSize': 14, 'fontWeight': 'normal', 'padding': (0, 0, 5, 0)},
        'caption': {'fontFamily': 'Segoe UI', 'fontSize': 12, 'fontWeight': 'normal', 'padding': (0, 0, 3, 0)},
    }

class FluentUIColors:
    TEXT_PRIMARY = '#323130'
    TEXT_SECONDARY = '#605E5C'
    BACKGROUND_LIGHT = '#FFFFFF'
    BACKGROUND_NEUTRAL_LIGHTER = '#F3F2F1'
    BORDER = '#8A8886'
    ACCENT = '#0078D4'
