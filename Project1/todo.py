# Import necessary modules
import tkinter as tk # Import tkinter for GUI elements
from tkinter import messagebox # Import messagebox for dialog boxes
import json # Import json module to handle saving and loading tasks
import os # Import os module to check for file existence

# Define the Task class
"""
        Initialize a new task instance with title, description, category, and completed status.
        :param title: The title of the task
        :param description: The description of the task
        :param category: The category of the task
        :param completed: Whether the task is completed (default is False)
"""
class Task:
    def __init__(self, title, description, category, completed=False): # Constructor method for initializing task attributes
        self.title = title # Set the title attribute
        self.description = description # Set the description attribute
        self.category = category # Set the category attribute
        self.completed = completed # Set the completed status (default is False)

# Function to save tasks to a JSON file
"""
    Save the list of tasks to a JSON file.
    :param tasks: List of Task objects
"""
def save_tasks(tasks):
    with open('tasks.json', 'w') as f: # Open 'tasks.json' in write mode
        json.dump([task.__dict__ for task in tasks], f) # Serialize task objects to dictionaries and save

# Function to load tasks from a JSON file
"""
    Load tasks from a JSON file if it exists; return an empty list if not.
    :return: List of Task objects
"""
def load_tasks():
    if not os.path.exists('tasks.json'):  # Check if the file exists
        return [] # Return an empty list if the file does not exist
    with open('tasks.json', 'r') as f:  # Open 'tasks.json' in read mode
        try:
            return [Task(**data) for data in json.load(f)] # Load JSON data and convert each dictionary to a Task object
        except json.JSONDecodeError:
            return []  # Return an empty list if JSON data is invalid

# Function to add a new task
"""
    Add a new task to the task list and update the display.
"""
def add_task():
    title = title_entry.get() # Get title from the title entry field
    description = description_entry.get() # Get description from the description entry field
    category = category_entry.get() # Get category from the category entry field
    
    if title: # Check if the title is not empty
        task = Task(title, description, category) # Create a new Task object
        tasks.append(task) # Add the new task to the tasks list
        save_tasks(tasks) # Save tasks to file
        update_task_list() # Update the task listbox display
        clear_entries() # Clear entry fields
        messagebox.showinfo("Success", "Task added successfully!") # Show success message
    else:
        messagebox.showwarning("Error", "Title is required to add a task.") # Show warning if title is missing

# Function to edit an existing task
def edit_task():
    selected_task = task_listbox.curselection() # Get the selected task index
    if selected_task: # Check if any task is selected
        index = selected_task[0] # Get the selected index
        task = tasks[index] # Get the selected task from tasks list
        
        # Populate the entries with the selected task details
        title_entry.delete(0, tk.END) # Clear title entry
        title_entry.insert(0, task.title) # Set title entry with task title
        
        description_entry.delete(0, tk.END) # Clear description entry
        description_entry.insert(0, task.description) # Set description entry with task description
        
        category_entry.delete(0, tk.END) # Clear category entry
        category_entry.insert(0, task.category) # Set category entry with task category
        
        # Update the button text and function
        add_button.config(text="Save Changes", command=lambda: save_edited_task(index)) # Set button to save changes
    else:
        messagebox.showwarning("Error", "Please select a task to edit.") # Show warning if no task selected

# Function to save changes to the edited task
def save_edited_task(index):
    title = title_entry.get() # Get the updated title from entry
    description = description_entry.get() # Get the updated description from entry
    category = category_entry.get() # Get the updated category from entry
    
    if title: # Check if the title is not empty
        tasks[index].title = title # Update the title of the task
        tasks[index].description = description # Update the description of the task
        tasks[index].category = category # Update the category of the task
        save_tasks(tasks) # Save tasks to file
        update_task_list() # Update the task listbox display
        clear_entries() # Clear entry fields
        messagebox.showinfo("Success", "Task edited successfully!") # Show success message
        
        # Reset the button back to add task mode
        add_button.config(text="Add Task", command=add_task) # Reset button to "Add Task"
    else:
        messagebox.showwarning("Error", "Title is required to save changes.") # Show warning if title is missing

# Function to update the task list display
def update_task_list():
    task_listbox.delete(0, tk.END) # Clear the listbox
    for i, task in enumerate(tasks): # Iterate over tasks with index
        status = "Completed" if task.completed else "Pending" # Set task status
        task_info = f"{i+1}. {task.title} - {task.description} ({task.category}) - {status}" # Create task info string
        task_listbox.insert(tk.END, task_info) # Insert task info into the listbox

# Function to mark a task as completed
def mark_task_completed():
    selected_task = task_listbox.curselection() # Get the selected task index
    if selected_task: # Check if any task is selected
        index = selected_task[0] # Get the selected index
        tasks[index].completed = True # Mark the task as completed
        save_tasks(tasks) # Save tasks to file
        update_task_list() # Update the task listbox display
        messagebox.showinfo("Success", "Task marked as completed!") # Show success message
    else:
        messagebox.showwarning("Error", "Please select a task to mark as completed.") # Show warning if no task selected

# Function to delete a task
def delete_task():
    selected_task = task_listbox.curselection() # Get the selected task index
    if selected_task: # Check if any task is selected
        index = selected_task[0] # Get the selected index
        del tasks[index] # Delete the task from the list
        save_tasks(tasks) # Save tasks to file
        update_task_list() # Update the task listbox display
        messagebox.showinfo("Success", "Task deleted successfully!") # Show success message
    else:
        messagebox.showwarning("Error", "Please select a task to delete.") # Show warning if no task selected

# Function to clear entry fields
def clear_entries():
    title_entry.delete(0, tk.END) # Clear the title entry field
    description_entry.delete(0, tk.END) # Clear the description entry field
    category_entry.delete(0, tk.END) # Clear the category entry field

# Set up the main application window
root = tk.Tk() # Create the main window
root.title("Personal To-Do List Application") # Set the window title

# Load existing tasks
tasks = load_tasks() # Load tasks from file

# Title Entry
tk.Label(root, text="Title:").grid(row=0, column=0, sticky=tk.W) # Create and position the title label
title_entry = tk.Entry(root, width=40) # Create the title entry field
title_entry.grid(row=0, column=1, columnspan=2) # Position the title entry field

# Description Entry
tk.Label(root, text="Description:").grid(row=1, column=0, sticky=tk.W) # Create and position the description label
description_entry = tk.Entry(root, width=40) # Create the description entry field
description_entry.grid(row=1, column=1, columnspan=2) # Position the description entry field

# Category Entry
tk.Label(root, text="Category:").grid(row=2, column=0, sticky=tk.W) # Create and position the category label
category_entry = tk.Entry(root, width=40) # Create the category entry field
category_entry.grid(row=2, column=1, columnspan=2) # Position the category entry field

# Buttons for task operations
add_button = tk.Button(root, text="Add Task", command=add_task) # Create "Add Task" button
add_button.grid(row=3, column=0, pady=10) # Position "Add Task" button

complete_button = tk.Button(root, text="Mark as Completed", command=mark_task_completed) # Create "Mark as Completed" button
complete_button.grid(row=3, column=1, pady=10) # Position "Mark as Completed" button

delete_button = tk.Button(root, text="Delete Task", command=delete_task) # Create "Delete Task" button
delete_button.grid(row=3, column=2, pady=10) # Position "Delete Task" button

edit_button = tk.Button(root, text="Edit Task", command=edit_task) # Create "Edit Task
edit_button.grid(row=3, column=3, pady=10) # Position "Edit Task" button

# Task Listbox to display tasks
task_listbox = tk.Listbox(root, width=60, height=15)
task_listbox.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

# Populate the task listbox with existing tasks
update_task_list()

# Run the main loop of the application
root.mainloop()