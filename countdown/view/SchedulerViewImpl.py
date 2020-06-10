import tkinter as tk

from countdown.presenter.SchedulerPresenter import SchedulerPresenter
from countdown.view.SchedulerViewMain import SchedulerViewMain
from countdown.view.SchedulerViewPresenter import SchedulerViewPresenter


class SchedulerViewImpl(SchedulerViewPresenter, SchedulerViewMain):

    def __init__(self, root):
        self.root = root
        self.font = ("Courier", 15)
        self.warning_font = ("Courier", 10)
        self.countdown_font = ("Courier", 23)
        self.padding_horizontal = 10
        self.padding_vertical = (10, 0)
        self.padding_vertical_last = (10, 10)

        self.__countdown_time = tk.Label(self.root, font=self.countdown_font)
        self.__countdown_time.grid(row=0, padx=self.padding_horizontal, pady=self.padding_vertical, sticky=tk.W,
                                   columnspan=2)

        tk.Label(self.root, text="Hours", font=self.font).grid(row=1, padx=self.padding_horizontal,
                                                               pady=self.padding_vertical, sticky=tk.W)
        self.__hours_input = tk.Entry(self.root, font=self.font)
        self.__hours_input.grid(row=1, column=1, padx=self.padding_horizontal, pady=self.padding_vertical)

        tk.Label(self.root, text="Minutes", font=self.font).grid(row=2, padx=self.padding_horizontal,
                                                                 pady=self.padding_vertical_last, sticky=tk.W)
        self.__minutes_input = tk.Entry(self.root, font=self.font)
        self.__minutes_input.grid(row=2, column=1, padx=self.padding_horizontal, pady=self.padding_vertical)

        self.__minutes_warning = tk.Label(self.root, text="Minutes input required", font=self.warning_font,
                                          foreground="red")

        self.__cancel_button = tk.Button(self.root, text="Cancel", font=self.font)
        self.__cancel_button.grid(row=4, column=0, sticky=tk.W, padx=self.padding_horizontal,
                                  pady=self.padding_vertical_last)
        self.__start_button = tk.Button(self.root, text="Start shutdown", font=self.font)
        self.__start_button.grid(row=4, column=1, sticky=tk.W, padx=self.padding_horizontal,
                                 pady=self.padding_vertical_last)

        self.presenter = SchedulerPresenter(self)
        self.input_validation = root.register(self.presenter.no_keypress_input_validation)

    def set_countdown_text(self, text):
        self.__countdown_time.config(text=text)

    def instantiate_buttons(self):
        self.__on_start_click()
        self.__on_cancel_click()
        self.__input_validation()
        self.on_close_window()

    def get_hours_input(self):
        return self.__hours_input.get()

    def get_minutes_input(self):
        return self.__minutes_input.get()

    def minutes_warning_visibility(self, is_visible: bool):
        if is_visible:
            self.__minutes_warning.grid(row=3, column=1, padx=self.padding_horizontal, sticky=tk.W)
        else:
            self.__minutes_warning.grid_remove()

    def __on_start_click(self):
        self.__start_button.configure(command=self.presenter.on_start_click)

    def __on_cancel_click(self):
        self.__cancel_button.configure(command=self.presenter.on_cancel_click)

    def __input_validation(self):
        self.__hours_input.configure(validate="key", validatecommand=(self.input_validation, "%P"))
        self.__minutes_input.configure(validate="key", validatecommand=(self.input_validation, "%P"))

    def on_close_window(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_destroy)

    def on_destroy(self):
        self.presenter.stop_countdown()
        self.root.destroy()
