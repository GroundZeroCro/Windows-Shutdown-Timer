import os
import threading
import time

from model.Scheduler import Scheduler
from view.SchedulerViewPresenter import SchedulerViewPresenter


class SchedulerPresenter:
    def __init__(self, view: SchedulerViewPresenter):
        self.thread_running = None
        self.thread = None
        self.view = view
        self.scheduled = Scheduler()

    def on_start_click(self):
        if self.view.get_minutes_input() == "":
            self.view.minutes_warning_visibility(True)
            return
        self.view.minutes_warning_visibility(False)
        self.__start_shutdown()

    def on_cancel_click(self):
        self.__cancel_shutdown()

    def valid_input(self, p):
        if p.isdigit() or p == "":
            return True
        return False

    def __start_shutdown(self):
        if self.__countdown_restarted():
            self.__cancel_shutdown()
            time.sleep(1)

        print("Started OS shutdown")
        self.thread_running = True
        self.thread = threading.Timer(0, self.__thread_worker, (int(self.__get_input_in_seconds()),))
        self.thread.start()

    def __countdown_restarted(self):
        return self.thread_running is True

    def __get_input_in_seconds(self):
        try:
            self.scheduled.hours = int(self.view.get_hours_input())
        except ValueError:
            self.scheduled.hours = 0
        self.scheduled.minutes = int(self.view.get_minutes_input())
        return self.scheduled.get_seconds()

    def __cancel_shutdown(self):
        print("Canceled OS shutdown")
        self.stop_countdown()
        self.thread.cancel()

    def stop_countdown(self):
        self.thread_running = False

    def __thread_worker(self, countdown_seconds):
        for i in range(countdown_seconds):
            if not self.thread_running:
                return
            seconds_remained = countdown_seconds - i
            print(self.scheduled.get_time_format(seconds_remained))
            self.view.set_countdown_text(self.scheduled.get_time_format(seconds_remained))
            time.sleep(1)
        self.__shut_windows_down()

    def __shut_windows_down(self):
        os.system("shutdown /p /f")
