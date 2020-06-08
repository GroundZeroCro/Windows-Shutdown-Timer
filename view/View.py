import tkinter as tk

root = tk.Tk()
font = ("Courier", 15)
padding_horizontal = 10
padding_vertical = (10, 0)
padding_vertical_last = (10, 10)


def start_shutdown():
    print("Starting windows shutdown")


def cancel_shutdown():
    print("Canceling windows shutdown")


tk.Label(root, text="Hours", font=font).grid(row=0, padx=padding_horizontal, pady=padding_vertical, sticky=tk.W)
hours_input = tk.Entry(root, font=font).grid(row=0, column=1, padx=padding_horizontal, pady=padding_vertical)

tk.Label(root, text="Minutes", font=font).grid(row=1, padx=padding_horizontal, pady=padding_vertical_last, sticky=tk.W)
minutes_input = tk.Entry(root, font=font).grid(row=1, column=1, padx=padding_horizontal, pady=padding_vertical)

tk.Button(root, text="Cancel", command=cancel_shutdown, font=font) \
    .grid(row=3, column=0, sticky=tk.W, padx=padding_horizontal, pady=padding_vertical_last)

tk.Button(root, text="Start shutdown", command=start_shutdown, font=font) \
    .grid(row=3, column=1, sticky=tk.W, padx=padding_horizontal, pady=padding_vertical_last)

root.mainloop()
