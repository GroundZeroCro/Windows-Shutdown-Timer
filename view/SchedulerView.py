import tkinter as tk


class SchedulerView:

    def __init__(self, root):
        self.root = root
        self.font = ("Courier", 15)
        self.padding_horizontal = 10
        self.padding_vertical = (10, 0)
        self.padding_vertical_last = (10, 10)
        tk.Label(self.root, text="Hours", font=self.font).grid(row=0, padx=self.padding_horizontal,
                                                               pady=self.padding_vertical, sticky=tk.W)
        hours_input = tk.Entry(self.root, font=self.font).grid(row=0, column=1, padx=self.padding_horizontal,
                                                               pady=self.padding_vertical)
        tk.Label(self.root, text="Minutes", font=self.font).grid(row=1, padx=self.padding_horizontal,
                                                                 pady=self.padding_vertical_last, sticky=tk.W)
        minutes_input = tk.Entry(self.root, font=self.font).grid(row=1, column=1, padx=self.padding_horizontal,
                                                                 pady=self.padding_vertical)
        self.cancel_button = tk.Button(self.root, text="Cancel", font=self.font)
        self.cancel_button.grid(row=3, column=0, sticky=tk.W, padx=self.padding_horizontal,
                                pady=self.padding_vertical_last)
        self.start_button = tk.Button(self.root, text="Start shutdown", font=self.font)
        self.start_button.grid(row=3, column=1, sticky=tk.W, padx=self.padding_horizontal,
                               pady=self.padding_vertical_last)

    def on_cancel_click(self, on_click):
        self.cancel_button.configure(command=on_click)

    def on_start_click(self, on_click):
        self.start_button.configure(command=on_click)
