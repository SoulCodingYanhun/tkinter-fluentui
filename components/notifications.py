import tkinter as tk
from tkinter import ttk
from ..core import FluentWidget
import time


class MessageBar(FluentWidget):
    def __init__(self, master=None, message="", type="info", duration=3000, **kwargs):
        super().__init__(master, **kwargs)
        self.message = message
        self.type = type
        self.duration = duration
        self.widget = ttk.Frame(master)
        self._create_widgets()

    def create_widget(self):
        return self.widget

    def _create_widgets(self):
        self.label = ttk.Label(self.widget, text=self.message, style=f"{self.type}.TLabel")
        self.label.pack(side=tk.LEFT, padx=(10, 5), pady=5)

        self.close_button = ttk.Button(self.widget, text="×", command=self.hide, style="Toolbutton")
        self.close_button.pack(side=tk.RIGHT, padx=(5, 10), pady=5)

    def show(self):
        self.widget.pack(fill=tk.X, padx=10, pady=(10, 0))
        if self.duration > 0:
            self.widget.after(self.duration, self.hide)

    def hide(self):
        self.widget.pack_forget()

    def set_message(self, message, type="info"):
        self.message = message
        self.type = type
        self.label.config(text=message, style=f"{type}.TLabel")


class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x = y = 0
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = ttk.Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack(ipadx=5, ipady=5)

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None


class Notification(FluentWidget):
    def __init__(self, master=None, title="", message="", duration=5000, **kwargs):
        super().__init__(master, **kwargs)
        self.title = title
        self.message = message
        self.duration = duration
        self.widget = tk.Toplevel(master)
        self._create_widgets()
        self._setup_animation()

    def create_widget(self):
        return self.widget

    def _create_widgets(self):
        self.widget.withdraw()
        self.widget.overrideredirect(True)

        main_frame = ttk.Frame(self.widget, style="Notification.TFrame")
        main_frame.pack(expand=True, fill=tk.BOTH)

        title_label = ttk.Label(main_frame, text=self.title, style="NotificationTitle.TLabel")
        title_label.pack(anchor="w", padx=10, pady=(10, 5))

        message_label = ttk.Label(main_frame, text=self.message, style="NotificationMessage.TLabel", wraplength=250)
        message_label.pack(anchor="w", padx=10, pady=(0, 10))

        close_button = ttk.Button(main_frame, text="×", command=self.hide, style="Toolbutton")
        close_button.place(relx=1.0, x=-5, y=5, anchor="ne")

    def _setup_animation(self):
        self.alpha = 0
        self.widget.attributes("-alpha", self.alpha)

        screen_width = self.widget.winfo_screenwidth()
        screen_height = self.widget.winfo_screenheight()
        notification_width = 300
        notification_height = 100
        x = screen_width - notification_width - 20
        y = screen_height - notification_height - 40
        self.widget.geometry(f"{notification_width}x{notification_height}+{x}+{y}")

    def show(self):
        self.widget.deiconify()
        self._fade_in()
        if self.duration > 0:
            self.widget.after(self.duration, self._fade_out)

    def hide(self):
        self._fade_out()

    def _fade_in(self):
        if self.alpha < 1.0:
            self.alpha += 0.1
            self.widget.attributes("-alpha", self.alpha)
            self.widget.after(20, self._fade_in)

    def _fade_out(self):
        if self.alpha > 0.0:
            self.alpha -= 0.1
            self.widget.attributes("-alpha", self.alpha)
            self.widget.after(20, self._fade_out)
        else:
            self.widget.withdraw()


class TeachingBubble(FluentWidget):
    def __init__(self, master, target, title, message, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.target = target
        self.title = title
        self.message = message
        self.command = command
        self.widget = tk.Toplevel(master)
        self._create_widgets()
        self._position_bubble()

    def create_widget(self):
        return self.widget

    def _create_widgets(self):
        self.widget.withdraw()
        self.widget.overrideredirect(True)

        main_frame = ttk.Frame(self.widget, style="TeachingBubble.TFrame")
        main_frame.pack(expand=True, fill=tk.BOTH)

        title_label = ttk.Label(main_frame, text=self.title, style="TeachingBubbleTitle.TLabel")
        title_label.pack(anchor="w", padx=10, pady=(10, 5))

        message_label = ttk.Label(main_frame, text=self.message, style="TeachingBubbleMessage.TLabel", wraplength=250)
        message_label.pack(anchor="w", padx=10, pady=(0, 10))

        if self.command:
            action_button = ttk.Button(main_frame, text="Learn more", command=self._on_action,
                                       style="TeachingBubble.TButton")
            action_button.pack(anchor="w", padx=10, pady=(0, 10))

        close_button = ttk.Button(main_frame, text="×", command=self.hide, style="Toolbutton")
        close_button.place(relx=1.0, x=-5, y=5, anchor="ne")

    def _position_bubble(self):
        self.widget.update_idletasks()
        target_x = self.target.winfo_rootx()
        target_y = self.target.winfo_rooty()
        target_height = self.target.winfo_height()
        bubble_width = self.widget.winfo_width()
        bubble_height = self.widget.winfo_height()

        # Position the bubble above the target by default
        x = target_x + (self.target.winfo_width() - bubble_width) // 2
        y = target_y - bubble_height - 10

        # If the bubble would go off the top of the screen, position it below the target instead
        if y < 0:
            y = target_y + target_height + 10

        self.widget.geometry(f"+{x}+{y}")

    def show(self):
        self.widget.deiconify()
        self._position_bubble()
        self.widget.lift()

    def hide(self):
        self.widget.withdraw()

    def _on_action(self):
        if self.command:
            self.command()
        self.hide()


def show_teaching_bubble(master, target, title, message, command=None):
    bubble = TeachingBubble(master, target, title, message, command)
    bubble.show()
    return bubble

def show_message(master, message, type="info", duration=3000):
    message_bar = MessageBar(master, message=message, type=type, duration=duration)
    message_bar.show()
    return message_bar


def show_notification(master, title, message, duration=5000):
    notification = Notification(master, title=title, message=message, duration=duration)
    notification.show()
    return notification


def add_tooltip(widget, text):
    return Tooltip(widget, text)
