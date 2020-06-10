import tkinter as tk
from unittest import TestCase
from unittest.mock import MagicMock, patch

from countdown.presenter.SchedulerPresenter import SchedulerPresenter
from countdown.view.SchedulerViewImpl import SchedulerViewImpl


class TestSchedulerPresenter(TestCase):

    def setUp(self):
        root = tk.Tk()
        self.mocked_view = SchedulerViewImpl(root)
        self.presenter = SchedulerPresenter(self.mocked_view)

    def tearDown(self):
        pass

    @patch.object(SchedulerViewImpl, 'minutes_warning_visibility')
    def test_minutes_input_missing_show_warning_message(self, minutes_warning_visibility):
        self.mocked_view.get_minutes_input = MagicMock(return_value="")
        self.assertFalse(self.presenter.has_minutes_input())
        minutes_warning_visibility.assert_called_once_with(True)

    @patch.object(SchedulerViewImpl, 'minutes_warning_visibility')
    def test_correct_minutes_input_asserts_true(self, minutes_warning_visibility):
        self.mocked_view.get_minutes_input = MagicMock(return_value=10)
        self.assertTrue(self.presenter.has_minutes_input())
        minutes_warning_visibility.assert_called_once_with(False)

    def test_key_press_only_digits_and_empty_asserts_true(self):
        self.assertTrue(self.presenter.no_keypress_input_validation("1"))
        self.assertTrue(self.presenter.no_keypress_input_validation(""))

    def test_key_press_only_digits_and_empty_asserts_false(self):
        self.assertFalse(self.presenter.no_keypress_input_validation("a"))

    def test_canceled_thread_running_asserts_false(self):
        self.mocked_view.get_minutes_input = MagicMock(return_value=10)
        self.presenter.on_start_click()
        self.presenter.thread.join()
        self.presenter.on_cancel_click()
        self.assertFalse(self.presenter.thread_running)
