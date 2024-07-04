# tkinter_fluentui/components/selectors.py

from ..core.base import FluentWidget
from ..core.styles import apply_theme, THEME_MANAGER
from ..utils.accessibility import KeyboardNavigable


class Checkbox(FluentWidget, KeyboardNavigable):
    def __init__(self, master, label, checked=False, command=None, **kwargs):
        super().__init__(master, width=200, height=30, **kwargs)
        self.label = label
        self.checked = checked
        self.command = command

        self.bind("<ButtonPress-1>", self._on_click)
        self.bind("<space>", self._on_click)

        apply_theme(self, bg='bg', fg='fg')
        self.redraw()

    def _on_click(self, event):
        self.checked = not self.checked
        self.redraw()
        if self.command:
            self.command()

    def _draw(self):
        super()._draw()
        width, height = self.winfo_width(), self.winfo_height()

        # 绘制复选框
        box_size = 20
        self.draw_rounded_rectangle(self, 5, (height - box_size) // 2, 5 + box_size, (height + box_size) // 2, 3,
                                    fill=THEME_MANAGER.get('accent') if self.checked else THEME_MANAGER.get('bg'),
                                    outline=THEME_MANAGER.get('fg'))

        # 绘制勾选标记
        if self.checked:
            self.create_line(8, height // 2, 13, height // 2 + 5, 22, height // 2 - 5, fill=THEME_MANAGER.get('bg'),
                             width=2)

        # 绘制标签
        font = THEME_MANAGER.get('font')
        self.create_text(30, height // 2, text=self.label, anchor="w", fill=THEME_MANAGER.get('fg'), font=font)


class RadioGroup(FluentWidget, KeyboardNavigable):
    def __init__(self, master, options, selected=None, command=None, **kwargs):
        super().__init__(master, width=200, height=30 * len(options), **kwargs)
        self.options = options
        self.selected = selected
        self.command = command

        self.bind("<ButtonPress-1>", self._on_click)
        self.bind("<Up>", self._on_up)
        self.bind("<Down>", self._on_down)

        apply_theme(self, bg='bg', fg='fg')
        self.redraw()

    def _on_click(self, event):
        y = event.y
        selected_index = y // 30
        if 0 <= selected_index < len(self.options):
            self.selected = self.options[selected_index]
            self.redraw()
            if self.command:
                self.command(self.selected)

    def _on_up(self, event):
        if self.selected:
            current_index = self.options.index(self.selected)
            if current_index > 0:
                self.selected = self.options[current_index - 1]
                self.redraw()
                if self.command:
                    self.command(self.selected)

    def _on_down(self, event):
        if self.selected:
            current_index = self.options.index(self.selected)
            if current_index < len(self.options) - 1:
                self.selected = self.options[current_index + 1]
                self.redraw()
                if self.command:
                    self.command(self.selected)

    def _draw(self):
        super()._draw()
        width, height = self.winfo_width(), self.winfo_height()

        for i, option in enumerate(self.options):
            y = i * 30

            # 绘制单选按钮
            self.create_oval(5, y + 5, 25, y + 25, outline=THEME_MANAGER.get('fg'))
            if option == self.selected:
                self.create_oval(9, y + 9, 21, y + 21, fill=THEME_MANAGER.get('accent'))

            # 绘制标签
            font = THEME_MANAGER.get('font')
            self.create_text(30, y + 15, text=option, anchor="w", fill=THEME_MANAGER.get('fg'), font=font)


class Dropdown(FluentWidget, KeyboardNavigable):
    def __init__(self, master, options, placeholder="Select an item", command=None, **kwargs):
        super().__init__(master, width=200, height=30, **kwargs)
        self.options = options
        self.placeholder = placeholder
        self.command = command
        self.selected = None
        self._open = False

        self.bind("<ButtonPress-1>", self._on_click)
        self.bind("<space>", self._on_click)

        apply_theme(self, bg='bg', fg='fg')
        self.redraw()

    def _on_click(self, event):
        self._open = not self._open
        if self._open:
            self._show_options()
        else:
            self._hide_options()
        self.redraw()

    def _show_options(self):
        options_window = tk.Toplevel(self)
        options_window.overrideredirect(True)
        options_window.geometry(f"200x{len(self.options) * 30}+{self.winfo_rootx()}+{self.winfo_rooty() + 30}")
        for option in self.options:
            btn = tk.Button(options_window, text=option, command=lambda o=option: self._select_option(o))
            btn.pack(fill=tk.X)

    def _hide_options(self):
        if self.winfo_children():
            self.winfo_children()[0].destroy()

    def _select_option(self, option):
        self.selected = option
        self._open = False
        self._hide_options()
        self.redraw()
        if self.command:
            self.command(self.selected)

    def _draw(self):
        super()._draw()
        width, height = self.winfo_width(), self.winfo_height()

        # 绘制下拉框
        self.draw_rounded_rectangle(self, 0, 0, width, height, THEME_MANAGER.get('radius', 5),
                                    fill=THEME_MANAGER.get('bg'), outline=THEME_MANAGER.get('fg'))

        # 绘制文本
        font = THEME_MANAGER.get('font')
        text = self.selected if self.selected else self.placeholder
        self.create_text(10, height // 2, text=text, anchor="w", fill=THEME_MANAGER.get('fg'), font=font)

        # 绘制箭头
        arrow_color = THEME_MANAGER.get('fg')
        self.create_polygon(width - 20, height // 2 - 5, width - 10, height // 2 - 5, width - 15, height // 2 + 5,
                            fill=arrow_color)


class Slider(FluentWidget, KeyboardNavigable):
    def __init__(self, master, min_value=0, max_value=100, value=50, command=None, **kwargs):
        super().__init__(master, width=200, height=30, **kwargs)
        self.min_value = min_value
        self.max_value = max_value
        self.value = value
        self.command = command

        self.bind("<ButtonPress-1>", self._on_click)
        self.bind("<B1-Motion>", self._on_drag)
        self.bind("<Left>", self._decrease)
        self.bind("<Right>", self._increase)

        apply_theme(self, bg='bg', fg='fg')
        self.redraw()

    def _on_click(self, event):
        self._update_value(event.x)

    def _on_drag(self, event):
        self._update_value(event.x)

    def _update_value(self, x):
        width = self.winfo_width() - 20  # 20 is the diameter of the slider thumb
        ratio = max(0, min(1, (x - 10) / width))
        self.value = self.min_value + ratio * (self.max_value - self.min_value)
        self.redraw()
        if self.command:
            self.command(self.value)

    def _decrease(self, event):
        self.value = max(self.min_value, self.value - 1)
        self.redraw()
        if self.command:
            self.command(self.value)

    def _increase(self, event):
        self.value = min(self.max_value, self.value + 1)
        self.redraw()
        if self.command:
            self.command(self.value)

    def _draw(self):
        super()._draw()
        width, height = self.winfo_width(), self.winfo_height()

        # 绘制滑动条轨道
        self.create_rectangle(10, height // 2 - 2, width - 10, height // 2 + 2, fill=THEME_MANAGER.get('fg'))

        # 绘制滑块
        ratio = (self.value - self.min_value) / (self.max_value - self.min_value)
        x = 10 + ratio * (width - 20)
        self.create_oval(x - 10, height // 2 - 10, x + 10, height // 2 + 10, fill=THEME_MANAGER.get('accent'))


class Switch(FluentWidget, KeyboardNavigable):
    def __init__(self, master, label="", on=False, command=None, **kwargs):
        super().__init__(master, width=60, height=30, **kwargs)
        self.label = label
        self.on = on
        self.command = command

        self.bind("<ButtonPress-1>", self._on_click)
        self.bind("<space>", self._on_click)

        apply_theme(self, bg='bg', fg='fg')
        self.redraw()

    def _on_click(self, event):
        self.on = not self.on
        self.redraw()
        if self.command:
            self.command(self.on)

    def _draw(self):
        super()._draw()
        width, height = self.winfo_width(), self.winfo_height()

        # 绘制开关背景
        bg_color = THEME_MANAGER.get('accent') if self.on else THEME_MANAGER.get('fg')
        self.draw_rounded_rectangle(self, 0, 0, width, height, height // 2, fill=bg_color)

        # 绘制开关滑块
        slider_x = width - 25 if self.on else 5
        self.create_oval(slider_x, 5, slider_x + 20, height - 5, fill=THEME_MANAGER.get('bg'))

        # 绘制标签
        if self.label:
            font = THEME_MANAGER.get('font')
            self.create_text(width + 10, height // 2, text=self.label, anchor="w", fill=THEME_MANAGER.get('fg'),
                             font=font)


class ColorPicker(FluentWidget, KeyboardNavigable):
    def __init__(self, master, color="#000000", command=None, **kwargs):
        super().__init__(master, width=200, height=30, **kwargs)
        self.color = color
        self.command = command

        self.bind("<ButtonPress-1>", self._on_click)
        self.bind("<space>", self._on_click)

        apply_theme(self, bg='bg', fg='fg')
        self.redraw()

    def _on_click(self, event):
        # 在实际应用中，这里应该打开一个颜色选择对话框
        # 由于tkinter没有内置的颜色选择器，这里我们只是循环预定义的颜色
        colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF']
        self.color = colors[(colors.index(self.color) + 1) % len(colors)]
        self.redraw()
        if self.command:
            self.command(self.color)

    def _draw(self):
        super()._draw()
        width, height = self.winfo_width(), self.winfo_height()

        # 绘制颜色预览框
        self.draw_rounded_rectangle(self, 5, 5, width - 5, height - 5, THEME_MANAGER.get('radius', 5),
                                    fill=self.color, outline=THEME_MANAGER.get('fg'))

        # 绘制颜色值文本
        font = THEME_MANAGER.get('font')
        self.create_text(width // 2, height // 2, text=self.color, fill=THEME_MANAGER.get('fg'), font=font)