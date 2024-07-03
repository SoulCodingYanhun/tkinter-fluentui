import tkinter as tk
from tkinter import ttk
from ..core.base import FluentComponent
from ..core.styles import FluentUIStyles, FluentUIColors

class FluentCheckbox(FluentComponent):
    def __init__(self, master=None, text="", checked=False, command=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.text = text
        self.checked = tk.BooleanVar(value=checked)
        self.command = command
        self.checkbox = None
        self._create_widget()

    def _create_widget(self):
        style = ttk.Style()
        style.configure(
            'Fluent.TCheckbutton',
            font=(FluentUIStyles.TYPOGRAPHY['body']['fontFamily'], 
                  FluentUIStyles.TYPOGRAPHY['body']['fontSize']),
            foreground=FluentUIColors.TEXT_PRIMARY,
            background=FluentUIColors.BACKGROUND_LIGHT,
            indicatorcolor=FluentUIColors.ACCENT,
            indicatorbackground=FluentUIColors.BACKGROUND_LIGHT,
        )

        self.checkbox = ttk.Checkbutton(
            self.master,
            text=self.text,
            variable=self.checked,
            style='Fluent.TCheckbutton',
            command=self.command
        )

        if self.id:
            self.checkbox.configure(id=self.id)
        if self.className:
            self.checkbox.configure(class_=self.className)

    def render(self):
        self.checkbox.pack(pady=5, padx=5, anchor='w')
        return self.checkbox

    def get_checked(self):
        return self.checked.get()

    def set_checked(self, state):
        self.checked.set(state)

class FluentRadioButton(FluentComponent):
    def __init__(self, master=None, text="", value=None, variable=None, command=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.text = text
        self.value = value
        self.variable = variable if variable else tk.StringVar()
        self.command = command
        self.radio_button = None
        self._create_widget()

    def _create_widget(self):
        style = ttk.Style()
        style.configure(
            'Fluent.TRadiobutton',
            font=(FluentUIStyles.TYPOGRAPHY['body']['fontFamily'], 
                  FluentUIStyles.TYPOGRAPHY['body']['fontSize']),
            foreground=FluentUIColors.TEXT_PRIMARY,
            background=FluentUIColors.BACKGROUND_LIGHT,
            indicatorcolor=FluentUIColors.ACCENT,
            indicatorbackground=FluentUIColors.BACKGROUND_LIGHT,
        )

        self.radio_button = ttk.Radiobutton(
            self.master,
            text=self.text,
            variable=self.variable,
            value=self.value,
            style='Fluent.TRadiobutton',
            command=self.command
        )

        if self.id:
            self.radio_button.configure(id=self.id)
        if self.className:
            self.radio_button.configure(class_=self.className)

    def render(self):
        self.radio_button.pack(pady=5, padx=5, anchor='w')
        return self.radio_button

class FluentCombobox(FluentComponent):
    def __init__(self, master=None, values=None, state="readonly", **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.values = values or []
        self.state = state
        self.combobox = None
        self._create_widget()

    def _create_widget(self):
        style = ttk.Style()
        style.configure(
            'Fluent.TCombobox',
            font=(FluentUIStyles.TYPOGRAPHY['body']['fontFamily'], 
                  FluentUIStyles.TYPOGRAPHY['body']['fontSize']),
            foreground=FluentUIColors.TEXT_PRIMARY,
            background=FluentUIColors.BACKGROUND_LIGHT,
            arrowcolor=FluentUIColors.ACCENT,
            bordercolor=FluentUIColors.BORDER,
        )

        self.combobox = ttk.Combobox(
            self.master,
            values=self.values,
            state=self.state,
            style='Fluent.TCombobox'
        )

        if self.id:
            self.combobox.configure(id=self.id)
        if self.className:
            self.combobox.configure(class_=self.className)

    def render(self):
        self.combobox.pack(pady=5, padx=5, fill=tk.X)
        return self.combobox

    def get_value(self):
        return self.combobox.get()

    def set_value(self, value):
        self.combobox.set(value)

class FluentSlider(FluentComponent):
    def __init__(self, master=None, from_=0, to=100, orient=tk.HORIZONTAL, command=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.from_ = from_
        self.to = to
        self.orient = orient
        self.command = command
        self.slider = None
        self._create_widget()

    def _create_widget(self):
        style = ttk.Style()
        style.configure(
            'Fluent.Horizontal.TScale',
            background=FluentUIColors.BACKGROUND_LIGHT,
            troughcolor=FluentUIColors.BACKGROUND_NEUTRAL_LIGHTER,
            slidercolor=FluentUIColors.ACCENT,
        )

        self.slider = ttk.Scale(
            self.master,
            from_=self.from_,
            to=self.to,
            orient=self.orient,
            style='Fluent.Horizontal.TScale',
            command=self.command
        )

        if self.id:
            self.slider.configure(id=self.id)
        if self.className:
            self.slider.configure(class_=self.className)

    def render(self):
        self.slider.pack(pady=5, padx=5, fill=tk.X)
        return self.slider

    def get_value(self):
        return self.slider.get()

    def set_value(self, value):
        self.slider.set(value)

# Assumed content of FluentUIStyles and FluentUIColors (you would define these in core/styles.py)
class FluentUIStyles:
    TYPOGRAPHY = {
        'body': {'fontFamily': 'Segoe UI', 'fontSize': 14},
    }

class FluentUIColors:
    TEXT_PRIMARY = '#323130'
    BACKGROUND_LIGHT = '#FFFFFF'
    BACKGROUND_NEUTRAL_LIGHTER = '#F3F2F1'
    BORDER = '#8A8886'
    ACCENT = '#0078D4'
