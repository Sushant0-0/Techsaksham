import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry

# Task List
tasks = []

def add_task(task, start_date, end_date, priority):
    tasks.append({"task": task, "completed": False, "start_date": start_date, "end_date": end_date, "priority": priority})
    update_task_list()

def delete_task(task_index):
    try:
        tasks.pop(task_index)
        update_task_list()
    except IndexError:
        messagebox.showerror("Error", "Invalid task number")

def mark_task_completed(task_index):
    try:
        tasks[task_index]["completed"] = True
        update_task_list()
    except IndexError:
        messagebox.showerror("Error", "Invalid task number")

def update_task_list():
    task_list.delete(0, tk.END)
    for i, task in enumerate(sorted(tasks, key=lambda x: x['priority'], reverse=True)):
        status = "✅" if task["completed"] else "❌"
        task_list.insert(tk.END, f'{i + 1}. {task["task"]} [{status}] (Priority: {task["priority"]})')

def add_task_command():
    task = task_entry.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    priority = priority_var.get()
    if task and start_date and end_date:
        add_task(task, start_date, end_date, priority)
        task_entry.delete(0, tk.END)
        start_date_entry.set_date("")
        end_date_entry.set_date("")
    else:
        messagebox.showwarning("Warning", "All fields must be filled!")

def delete_task_command():
    try:
        selected_task_index = task_list.curselection()[0]
        delete_task(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected")

def mark_task_completed_command():
    try:
        selected_task_index = task_list.curselection()[0]
        mark_task_completed(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected")

def toggle_theme():
    current_theme = root.tk.call("ttk::style", "theme", "use")
    new_theme = "clam" if current_theme == "alt" else "alt"
    root.tk.call("ttk::style", "theme", "use", new_theme)

# UI Setup
root = tk.Tk()
root.title("🔥 Lit Task Manager 🔥")
root.geometry("700x500")
root.configure(bg="#222")

# Custom Styling
style = ttk.Style()
style.theme_use("alt")
style.configure("TButton", font=("Arial", 12, "bold"), padding=10, foreground="white", background="#ff5733")
style.configure("TLabel", font=("Arial", 12, "bold"), background="#222", foreground="white")
style.configure("TFrame", background="#222")

frame = ttk.Frame(root)
frame.pack(pady=10)

task_entry = ttk.Entry(frame, width=50)
task_entry.grid(row=0, column=0, padx=5)

priority_label = ttk.Label(frame, text="Priority:")
priority_label.grid(row=0, column=1, padx=5)
priority_var = tk.IntVar(value=1)
priority_menu = ttk.Combobox(frame, textvariable=priority_var, values=(1, 2, 3, 4, 5), width=5)
priority_menu.grid(row=0, column=2, padx=5)

start_date_entry = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2)
start_date_entry.grid(row=1, column=0, padx=5, pady=5)
end_date_entry = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2)
end_date_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = ttk.Button(frame, text="🔥 Add Task", command=add_task_command)
add_button.grid(row=0, column=3, padx=5)

task_list = tk.Listbox(root, width=80, height=15, bg="#333", fg="white")
task_list.pack(pady=10)

button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

delete_button = ttk.Button(button_frame, text="🗑 Delete", command=delete_task_command)
delete_button.grid(row=0, column=0, padx=5)

complete_button = ttk.Button(button_frame, text="✅ Complete", command=mark_task_completed_command)
complete_button.grid(row=0, column=1, padx=5)

theme_button = ttk.Button(button_frame, text="🌙 Toggle Theme", command=toggle_theme)
theme_button.grid(row=0, column=2, padx=5)

update_task_list()

root.mainloop()
