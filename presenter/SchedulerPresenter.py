import threading
import time

from view.SchedulerView import SchedulerView


class SchedulerPresenter():
    def __init__(self, view):
        self.thread_running = True
        self.thread = None
        self.view: SchedulerView = view

    def instantiate_buttons(self):
        self.view.on_start_click(self.__start_shutdown)
        self.view.on_cancel_click(self.__cancel_shutdown)

    def __start_shutdown(self):
        print("Started OS shutdown")
        self.thread_running = True
        self.thread = threading.Timer(0, self.__thread_worker, (10,))
        self.thread.start()

    def __cancel_shutdown(self):
        print("Canceled OS shutdown")
        self.thread_running = False
        self.thread.cancel()

    def __thread_worker(self, countdown_seconds):
        for i in range(countdown_seconds):
            if not self.thread_running:
                return
            print(i)
            time.sleep(1)
        print("Shutting down OS")
