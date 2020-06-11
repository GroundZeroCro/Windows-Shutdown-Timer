import tkinter as tk
from unittest import TestCase
from unittest.mock import patch, MagicMock

from countdown.presenter.SchedulerPresenter import SchedulerPresenter
from countdown.view.SchedulerViewImpl import SchedulerViewImpl


class TestSchedulerViewImpl(TestCase):

    def setUp(self):
        root = tk.Tk()
        self.view = SchedulerViewImpl(root)

    @patch.object(SchedulerPresenter, 'stop_countdown')
    def test_on_destroy_stops_countdown(self, on_destroy):
        self.view.on_destroy()
        on_destroy.assert_called_once_with()

    @patch.object(tk.Tk, 'destroy')
    def test_on_destroy_destroys_tkinter_root(self, root):
        self.view.on_destroy()
        root.assert_called_once_with()

    @patch.object(tk.Tk, 'protocol')
    def test_on_close_windows_calls_correct_function(self, root):
        self.view.on_close_window()
        root.assert_called_once_with('WM_DELETE_WINDOW', self.view.on_destroy)
