import tkinter as tk

from countdown.view.SchedulerViewImpl import SchedulerViewImpl
from countdown.view import SchedulerViewMain

root = tk.Tk()
view: SchedulerViewMain = SchedulerViewImpl(root)
view.instantiate_buttons()
root.mainloop()
