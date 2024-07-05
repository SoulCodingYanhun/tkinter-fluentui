import tkinter as tk
from tkinter import ttk
from ..core import FluentWidget


class DetailsList(FluentWidget):
    def __init__(self, master=None, columns=None, data=None, **kwargs):
        super().__init__(master, **kwargs)
        self.columns = columns or []
        self.data = data or []
        self.widget = ttk.Frame(master)
        self._create_list()

    def create_widget(self):
        return self.widget

    def _create_list(self):
        self.tree = ttk.Treeview(self.widget, columns=self.columns, show="headings", style="Fluent.Treeview")
        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=100)

        for item in self.data:
            self.tree.insert("", "end", values=item)

        self.tree.pack(expand=True, fill="both")

        scrollbar = ttk.Scrollbar(self.widget, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

    def add_item(self, item):
        self.tree.insert("", "end", values=item)

    def clear(self):
        for item in self.tree.get_children():
            self.tree.delete(item)


class GroupedList(FluentWidget):
    def __init__(self, master=None, groups=None, **kwargs):
        super().__init__(master, **kwargs)
        self.groups = groups or []
        self.widget = ttk.Frame(master)
        self._create_list()

    def create_widget(self):
        return self.widget

    def _create_list(self):
        self.tree = ttk.Treeview(self.widget, show="tree", style="Fluent.Treeview")
        for group in self.groups:
            group_id = self.tree.insert("", "end", text=group['name'])
            for item in group['items']:
                self.tree.insert(group_id, "end", text=item)

        self.tree.pack(expand=True, fill="both")

        scrollbar = ttk.Scrollbar(self.widget, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

    def add_group(self, name, items):
        group_id = self.tree.insert("", "end", text=name)
        for item in items:
            self.tree.insert(group_id, "end", text=item)

    def clear(self):
        for item in self.tree.get_children():
            self.tree.delete(item)


class List(FluentWidget):
    def __init__(self, master=None, items=None, **kwargs):
        super().__init__(master, **kwargs)
        self.items = items or []
        self.widget = ttk.Frame(master)
        self._create_list()

    def create_widget(self):
        return self.widget

    def _create_list(self):
        self.listbox = tk.Listbox(self.widget, selectmode=tk.SINGLE, activestyle='none')
        for item in self.items:
            self.listbox.insert(tk.END, item)

        self.listbox.pack(expand=True, fill="both")

        scrollbar = ttk.Scrollbar(self.widget, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.configure(yscrollcommand=scrollbar.set)

    def add_item(self, item):
        self.listbox.insert(tk.END, item)

    def clear(self):
        self.listbox.delete(0, tk.END)

    def get_selected(self):
        return self.listbox.get(self.listbox.curselection())
