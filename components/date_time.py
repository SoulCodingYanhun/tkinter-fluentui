import tkinter as tk
from tkinter import ttk
import calendar
from datetime import date, datetime
from ..core import FluentWidget

class Calendar(FluentWidget):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.widget = ttk.Frame(master)
        self._setup_calendar()

    def create_widget(self):
        return self.widget

    def _setup_calendar(self):
        self.year = date.today().year
        self.month = date.today().month

        self.header = ttk.Label(self.widget, text=self._get_header())
        self.header.pack(pady=10)

        self.cal = ttk.Treeview(self.widget, show='', selectmode='none', height=7)
        self.cal.pack()

        self._update_calendar()

        prev_button = ttk.Button(self.widget, text="<", command=self._prev_month)
        next_button = ttk.Button(self.widget, text=">", command=self._next_month)
        prev_button.pack(side=tk.LEFT)
        next_button.pack(side=tk.RIGHT)

    def _get_header(self):
        return f"{calendar.month_name[self.month]} {self.year}"

    def _update_calendar(self):
        self.header.config(text=self._get_header())

        self.cal.delete(*self.cal.get_children())

        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        self.cal.insert("", "end", values=days)

        for week in calendar.monthcalendar(self.year, self.month):
            self.cal.insert("", "end", values=week)

    def _prev_month(self):
        self.month -= 1
        if self.month < 1:
            self.month = 12
            self.year -= 1
        self._update_calendar()

    def _next_month(self):
        self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1
        self._update_calendar()


class DatePicker(FluentWidget):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.widget = ttk.Frame(master)
        self.selected_date = None
        self._create_widgets()

    def create_widget(self):
        return self.widget

    def _create_widgets(self):
        self.entry = ttk.Entry(self.widget, width=10)
        self.entry.pack(side=tk.LEFT, padx=(0, 5))

        self.button = ttk.Button(self.widget, text="📅", width=3, command=self._show_calendar)
        self.button.pack(side=tk.LEFT)

        self.calendar_popup = None

    def _show_calendar(self):
        if self.calendar_popup is None or not self.calendar_popup.winfo_exists():
            self.calendar_popup = tk.Toplevel(self.widget)
            self.calendar_popup.withdraw()  # Hide initially
            self.calendar_popup.overrideredirect(True)

            self.calendar = Calendar(self.calendar_popup)
            self.calendar.widget.pack(padx=5, pady=5)

            select_button = ttk.Button(self.calendar_popup, text="Select", command=self._on_date_select)
            select_button.pack(pady=(0, 5))

            self.calendar_popup.bind("<FocusOut>", self._on_focus_out)

        # Position the calendar popup
        x = self.widget.winfo_rootx()
        y = self.widget.winfo_rooty() + self.widget.winfo_height()
        self.calendar_popup.geometry(f"+{x}+{y}")

        self.calendar_popup.deiconify()  # Show the popup
        self.calendar_popup.focus_set()

    def _on_date_select(self):
        selected = self.calendar.cal.selection_get()
        if selected:
            self.selected_date = selected
            self.entry.delete(0, tk.END)
            self.entry.insert(0, selected.strftime("%Y-%m-%d"))
        self._hide_calendar()

    def _on_focus_out(self, event):
        # Check if the new focus is outside of the calendar popup
        if event.widget == self.calendar_popup and not any(
                child.winfo_containing(event.x_root, event.y_root) == child for child in
                self.calendar_popup.winfo_children()):
            self._hide_calendar()

    def _hide_calendar(self):
        if self.calendar_popup and self.calendar_popup.winfo_exists():
            self.calendar_popup.withdraw()

    def get_date(self):
        return self.selected_date

    def set_date(self, date):
        if isinstance(date, datetime):
            self.selected_date = date
            self.entry.delete(0, tk.END)
            self.entry.insert(0, date.strftime("%Y-%m-%d"))