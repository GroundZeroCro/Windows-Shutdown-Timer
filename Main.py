import tkinter as tk

from presenter.SchedulerPresenter import SchedulerPresenter
from view.SchedulerView import SchedulerView

root = tk.Tk()
view = SchedulerView(root)
presenter = SchedulerPresenter(view)
presenter.instantiate_buttons()
root.mainloop()
