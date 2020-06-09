import threading
import time

from model.Scheduler import Scheduler
from view.SchedulerView import SchedulerView


class SchedulerPresenter():
    def __init__(self, view):
        self.thread_running = True
        self.thread = None
        self.view: SchedulerView = view

        self.scheduled = Scheduler()

    def instantiate_buttons(self):
        self.view.on_start_click(self.__start_shutdown)
        self.view.on_cancel_click(self.__cancel_shutdown)

    def __get_input_in_seconds(self):
        self.scheduled.hours = int(self.view.get_hours_input())
        self.scheduled.minutes = int(self.view.get_minutes_input())
        return self.scheduled.get_seconds()

    def __start_shutdown(self):
        print(self.__get_input_in_seconds())
        print("Started OS shutdown")
        self.thread_running = True
        self.thread = threading.Timer(0, self.__thread_worker, (self.__get_input_in_seconds(),))
        self.thread.start()

    def __cancel_shutdown(self):
        print("Canceled OS shutdown")
        self.thread_running = False
        self.thread.cancel()

    def __thread_worker(self, countdown_seconds):
        for i in range(countdown_seconds):
            if not self.thread_running:
                return
            seconds_remained = countdown_seconds - i
            print(self.scheduled.get_time_format(seconds_remained))
            time.sleep(1)
        print("Shutting down OS")
