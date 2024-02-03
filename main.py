import tkinter as tk
from tkinter import messagebox

try:
    with open("tasks.txt", "r") as f:
        pass
except FileNotFoundError:
    with open("tasks.txt", "w") as f:
        pass


# Save tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as f:
        tasks = listbox.get(0, listbox.size())
        for task in tasks:
            f.write(task + "\n")
    messagebox.showinfo("Info", "Tasks are saved successfully.")


# Add a task
def add_task():
    task = entry.get()
    if task:
        if task not in listbox.get(0, tk.END):  # Check for duplicates
            listbox.insert(tk.END, task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "This task already exists.")
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


# Delete a task
def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:  # Specify the exception
        messagebox.showwarning("Warning", "Please select a task to delete.")


# Clear all tasks
def clear_tasks():
    listbox.delete(0, tk.END)
    messagebox.showinfo("Info", "All tasks are deleted successfully.")


# Create a root window
root = tk.Tk()
root.title("To-Do List")
root.resizable(0, 0)

# Create a label
tk.Label(root, text="To-Do List", font=("Arial", 24)).pack(expand=3, padx=100, pady=25)


# Create a frame for the listbox
frame = tk.Frame(root)
frame.pack(pady=10)

# Create a scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a listbox
listbox = tk.Listbox(
    frame, width=50, height=10, font=("Arial", 12), yscrollcommand=scrollbar.set
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=listbox.yview)

# Create an entry box
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

# Create buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks)
clear_button.pack(pady=5)

# Load tasks from a file
with open("tasks.txt", "r") as f:
    tasks = f.readlines()
    for task in tasks:
        listbox.insert(tk.END, task)


# Create a binding on the root window
root.bind("<Return>", add_task)

# Create a menu
my_menu = tk.Menu(root)
root.config(menu=my_menu)
file_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save Tasks", command=save_tasks)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
help_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(
    label="About",
    command=lambda: messagebox.showinfo(
        "About",
        "This is a To-Do List app made using Tkinter.\n\nMade by @jaguar000212",
    ),
)
help_menu.add_command(
    label="Help",
    command=lambda: messagebox.showinfo(
        "Help",
        "Add a task by typing it in the entry box and pressing the 'Add Task' button or pressing the 'Enter' key.\n\nDelete a task by selecting it and pressing the 'Delete Task' button.\n\nClear all tasks by pressing the 'Clear All Tasks' button.\n\nSave all tasks by pressing the 'Save Tasks' button.\n\nExit the app by pressing the 'Exit' button or by pressing the 'X' button on the top right corner of the window.\n\nMade by @jaguar000212",
    ),
)


# Create the footer
footer = tk.Label(root, text="Made by @jaguar000212\n♥️♥️♥️", anchor="center")
footer.configure(
    font=(
        "Arial",
        10,
        "bold",
    ),
    fg="red",
    cursor="hand2",
    pady=10,
    padx=10,
)
footer.pack(expand=3, padx=100, pady=25)

# Run the root window's main loop
root.mainloop()
