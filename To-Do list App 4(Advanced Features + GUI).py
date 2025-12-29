#To-Do List App with added features and more fancier GUI

import tkinter as tk
from tkinter import messagebox
import os

tasks = []
FILENAME = "tasks.txt"

def load_tasks():
    global tasks
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            lines = f.readlines()
            tasks = []
            for line in lines:
                text, status = line.strip().split("|")
                tasks.append({"task": text, "done": status == "done"})
    update_listbox()

def save_tasks():
    with open(FILENAME, "w") as f:
        for t in tasks:
            status = "done" if t["done"] else "not"
            f.write(f"{t['task']} | {status}\n")

def update_listbox(filtered = None):
    listbox.delete(0, tk.END)
    display_tasks = filtered if filtered is not None else tasks
    for i, task in enumerate(display_tasks, 1):
        status = "DONE"if task["done"] else "NOT DONE"
        listbox.insert(tk.END, f"{i}. {task['task']}[{status}]")

def add_task():
    task_text = entry.get()
    if task_text:
        tasks.append({"task": task_text, "done": False})
        entry.delete(0, tk.END)
        update_listbox()
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def mark_done():
    try:
       index = listbox.curselection()[0]
       tasks[index]["done"] = True
       update_listbox()
       save_tasks()
    except IndexError:
       messagebox.showwarning("Warning", "Please select a task to mark as done!")

def clear_all():
    global tasks
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        tasks = []
        update_listbox()
        save_tasks()

def search_task():
    query = search_entry.get().lower()
    if query:
        filtered = [t for t in tasks if query in t["task"].lower()]
        update_listbox(filtered)
    else:
        update_listbox()
        
        

# GUI setup
root = tk.Tk()
root.title("Baymax To-Do App")
root.geometry("700x700")
root.config(bg = "#f0f8ff") #light background

#Title
title = tk.Label(root, text = "My To-Do List", font = ("Arial", 18, "bold"),bg = "#f0f8ff", fg = "#2c3e50")
title.pack(pady = 10)

#Entry for new tasks
entry = tk.Entry(root, width = 70, font = ("Arial", 12))
entry.pack(pady = 10)

#Buttons
frame = tk.Frame(root, bg = "#f0f8ff")
frame.pack()

btn_add = tk.Button(frame, text = "Add Task", command = add_task, bg = "#2ecc71", fg = "white", font = ("Arial", 10, "bold"))
btn_add.pack(side = tk.LEFT, padx = 5)

btn_delete = tk.Button(frame, text = "Delete Task", command = delete_task, bg = "#e74c3c", fg = "white", font = ("Arial", 10, "bold"))
btn_delete.pack(side = tk.LEFT, padx = 5)

btn_done = tk.Button(frame, text = "Mark Done", command = mark_done, bg = "#3498db", fg = "white", font = ("Arial", 10, "bold"))
btn_done.pack(side = tk.LEFT, padx = 5)

btn_clear = tk.Button(frame, text = "Clear All", command = clear_all, bg = "#9b59b6", fg = "white", font = ("Arial", 10, "bold"))
btn_clear.pack(side = tk.LEFT, padx = 5)

#Task list
listbox = tk.Listbox(root, width = 70, height = 20, font = ("Consolas", 12))
listbox.pack(pady = 10)

#Search bar
search_frame = tk.Frame(root, bg = "#f0f8ff")
search_frame.pack(pady = 5)

search_entry = tk.Entry(search_frame, width = 50, font = ("Arial", 12))
search_entry.pack(side = tk.LEFT, padx = 5)

btn_search = tk.Button(search_frame, text = "Search", command = search_task, bg = "#f39c12", fg = "white", font = ("Arial", 10, "bold"))
btn_search.pack(side = tk.LEFT)

#Load tasks when app starts
load_tasks()

root.mainloop()
