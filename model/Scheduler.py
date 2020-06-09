import datetime
from dataclasses import dataclass


@dataclass
class Scheduler:
    hours: int = 0
    minutes: int = 0

    def get_seconds(self):
        return self.hours * 60 * 60 + self.minutes * 60

    def get_time_format(self, seconds: int):
        time = str(datetime.timedelta(seconds=seconds))
        return "Shutdown in %s" % time
