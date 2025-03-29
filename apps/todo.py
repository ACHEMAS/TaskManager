# /Users/mac/PYTHON/todo.py
import tkinter as tk
from tkinter import messagebox
from styles import setup_ui  # Import UI setup from styles.py

# List to store tasks
tasks = []

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        entry.delete(0, tk.END)
        status_label.config(text="Task added!")
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Function to remove a task
def remove_task():
    selected = task_list.curselection()
    if selected:
        task_index = selected[0]
        removed_task = tasks.pop(task_index)
        update_task_list()
        status_label.config(text=f"'{removed_task}' removed!")
    else:
        messagebox.showwarning("Warning", "Please select a task to remove!")

# Function to update the task list display
def update_task_list():
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks, 1):
        task_list.insert(tk.END, f"{i}. {task}")

# Create the main window and set up UI
window = tk.Tk()
entry, task_list, status_label = setup_ui(window, add_task, remove_task)  # Get widgets from styles.py

# Start the application
window.mainloop()