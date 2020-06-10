import datetime
from unittest import TestCase

from countdown.model.Scheduler import Scheduler


class TestScheduler(TestCase):
    def setUp(self):
        self.scheduler = Scheduler()

    def test_seconds_asserts_equals(self):
        self.scheduler.hours = 1
        self.scheduler.minutes = 1
        expected = self.scheduler.hours * 60 * 60 + self.scheduler.minutes * 60
        self.assertEqual(expected, self.scheduler.get_seconds())

    def test_time_format_asserts_true(self):
        seconds = 60
        expected = "Shutdown in %s" % str(datetime.timedelta(seconds=seconds))
        self.assertEqual(expected, self.scheduler.get_time_format(seconds))
