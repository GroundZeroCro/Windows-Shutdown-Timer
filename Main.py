import tkinter as tk

from view.SchedulerViewImpl import SchedulerViewImpl
from view.SchedulerViewMain import SchedulerViewMain

root = tk.Tk()
view: SchedulerViewMain = SchedulerViewImpl(root)
view.instantiate_buttons()
root.mainloop()
