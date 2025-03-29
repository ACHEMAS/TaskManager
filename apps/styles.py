# /Users/mac/PYTHON/styles.py
import tkinter as tk

def setup_ui(window, add_task_callback, remove_task_callback):
    # Window properties
    window.title("To-Do List Manager")
    window.geometry("400x500")

    # Create GUI elements with styles
    label = tk.Label(
        window,
        text="Enter a Task:",
        font=("Arial", 12)
    )
    label.pack(pady=10)

    entry = tk.Entry(
        window,
        width=30
    )
    entry.pack(pady=5)

    add_button = tk.Button(
        window,
        text="Add Task",
        command=add_task_callback,  # Link to logic function
        font=("Arial", 12)
    )
    add_button.pack(pady=5)

    task_list = tk.Listbox(
        window,
        height=15,
        width=40
    )
    task_list.pack(pady=10)

    remove_button = tk.Button(
        window,
        text="Remove Task",
        command=remove_task_callback,  # Link to logic function
        font=("Arial", 12)
    )
    remove_button.pack(pady=5)

    quit_button = tk.Button(
        window,
        text="Quit",
        command=window.quit,
        font=("Arial", 12)
    )
    quit_button.pack(pady=5)

    status_label = tk.Label(
        window,
        text="",
        font=("Arial", 12),
        fg="green"
    )
    status_label.pack(pady=10)

    # Return widgets needed by todo.py
    return entry, task_list, status_label