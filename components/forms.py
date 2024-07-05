from tkinter import ttk
from ..core import FluentWidget


class Form(FluentWidget):
    def __init__(self, master=None, fields=None, **kwargs):
        super().__init__(master, **kwargs)
        self.widget = ttk.Frame(master)
        self.fields = fields or []
        self._create_fields()

    def create_widget(self):
        return self.widget

    def _create_fields(self):
        for i, field in enumerate(self.fields):
            label = ttk.Label(self.widget, text=field['label'])
            label.grid(row=i, column=0, padx=5, pady=5, sticky='e')

            if field['type'] == 'entry':
                widget = ttk.Entry(self.widget)
            elif field['type'] == 'text':
                widget = ttk.Text(self.widget, height=3)
            elif field['type'] == 'combobox':
                widget = ttk.Combobox(self.widget, values=field.get('values', []))
            else:
                widget = ttk.Entry(self.widget)  # Default to Entry

            widget.grid(row=i, column=1, padx=5, pady=5, sticky='we')
            field['widget'] = widget

    def get_values(self):
        return {field['name']: field['widget'].get() for field in self.fields}
