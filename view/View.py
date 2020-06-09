import threading
import time
import tkinter as tk

root = tk.Tk()
font = ("Courier", 15)
padding_horizontal = 10
padding_vertical = (10, 0)
padding_vertical_last = (10, 10)

thread_running = True
thread = None


def start_shutdown():
    print("Starting windows shutdown")
    global thread_running
    global thread
    thread_running = True
    thread = threading.Timer(0, thread_worker, (10,))
    thread.start()


def cancel_shutdown():
    print("Canceling windows shutdown")
    global thread_running
    global thread
    thread_running = False
    thread.cancel()


def thread_worker(countdown_seconds):
    for i in range(countdown_seconds):
        if not thread_running:
            return
        print(i)
        time.sleep(1)
    print("Shutting down OS")


tk.Label(root, text="Hours", font=font).grid(row=0, padx=padding_horizontal, pady=padding_vertical, sticky=tk.W)
hours_input = tk.Entry(root, font=font).grid(row=0, column=1, padx=padding_horizontal, pady=padding_vertical)

tk.Label(root, text="Minutes", font=font).grid(row=1, padx=padding_horizontal, pady=padding_vertical_last, sticky=tk.W)
minutes_input = tk.Entry(root, font=font).grid(row=1, column=1, padx=padding_horizontal, pady=padding_vertical)

tk.Button(root, text="Cancel", command=cancel_shutdown, font=font) \
    .grid(row=3, column=0, sticky=tk.W, padx=padding_horizontal, pady=padding_vertical_last)

tk.Button(root, text="Start shutdown", command=start_shutdown, font=font) \
    .grid(row=3, column=1, sticky=tk.W, padx=padding_horizontal, pady=padding_vertical_last)

root.mainloop()
