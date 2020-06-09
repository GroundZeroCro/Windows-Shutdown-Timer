import tkinter as tk

from view.SchedulerView import SchedulerView

root = tk.Tk()
view = SchedulerView(root)
view.instantiate_buttons()
root.mainloop()
