# Personal To-Do List Application
This is a simple To-Do List application built with Python and Tkinter, designed to help you organize and manage tasks efficiently. With this application, you can add, edit, complete, and delete tasks, each with a title, description, and category.

## Features

- Add a Task: Input a title, description, and category, then click "Add Task" to save it to the list.
- Edit a Task: Select a task from the list and click "Edit Task" to populate the fields with the current details. After making changes, click "Save Changes" to update the task.
- Mark as Completed: Select a task and click "Mark as Completed" to mark the task as done.
- Delete a Task: Select a task and click "Delete Task" to remove it from the list.
- Persistent Storage: All tasks are saved to a tasks.json file, allowing you to reload your task list each time you run the application.


Usage

1. Adding a Task: Enter a title (required), description, and category for your task. Click "Add Task" to add it to the list.


2. Editing a Task:

Select a task from the list.

Click "Edit Task" to populate the title, description, and category fields with the selected task’s details.

Make your edits and click "Save Changes." This updates the task and resets the button back to "Add Task" mode.



3. Completing a Task:

Select a task from the list.

Click "Mark as Completed." The task will be updated with a "Completed" status.



4. Deleting a Task:

Select a task from the list.

Click "Delete Task" to remove it from the list.



5. Viewing Tasks:

All tasks will display in the listbox with the format:

Task Number. Title (Category) - Status

The status will either be "Completed" or "Pending."




Code Explanation

Task Class

This class defines the task object with the following attributes:

title (string): Title of the task.

description (string): Description of the task.

category (string): Category of the task.

completed (boolean): Status of the task, either completed or pending.


Functions

1. save_tasks(tasks)

Purpose: Saves the current list of tasks to a JSON file (tasks.json) for persistent storage.

Parameters:

tasks: A list of Task objects to be saved.


Functionality:

Opens tasks.json in write mode.

Converts each task to a dictionary (using _dict_) and writes the list of dictionaries to the file.


Usage:

Called after adding, editing, or deleting a task to update the saved list of tasks.



2. load_tasks()

Purpose: Loads tasks from the tasks.json file at the start of the application, allowing for persistent storage.

Returns:

A list of Task objects if tasks are loaded successfully, or an empty list if the file does not exist or is unreadable.


Functionality:

Checks if tasks.json exists.

Reads and parses the file content as JSON. Each item is used to instantiate a Task object, and all tasks are returned as a list.

Handles JSON decoding errors gracefully by returning an empty list if the file cannot be read correctly.


Usage:

Called once at the start of the application to initialize the tasks list with saved tasks.



3. add_task()

Purpose: Adds a new task to the list based on user input in the title, description, and category fields.

Functionality:

Reads the values from the input fields (title, description, and category).

Checks if the title field is not empty. If it is, a warning message is displayed.

Creates a new Task object with the provided details, appends it to the tasks list, saves the updated list, and updates the task display.

Clears the input fields after adding the task.


Usage:

Called when the user clicks the "Add Task" button.



4. edit_task()

Purpose: Prepares the application to edit a selected task by populating the input fields with the task’s current details.

Functionality:

Checks if a task is selected in the task_listbox.

Retrieves the selected task based on its index in the list.

Populates the title, description, and category input fields with the task's current values.

Changes the text of the add_button to "Save Changes" and updates its command to call save_edited_task with the selected task’s index.

If no task is selected, displays a warning message.


Usage:

Called when the user clicks the "Edit Task" button.



5. save_edited_task(index)

Purpose: Saves changes made to an existing task and reverts the "Save Changes" button back to "Add Task."

Parameters:

index: The index of the task in the tasks list being edited.


Functionality:

Retrieves updated values from the input fields.

Updates the task at the given index in the tasks list with the new values.

Saves the updated list of tasks and refreshes the task display.

Clears the input fields and resets the add_button text to "Add Task" and its command to add_task.


Usage:

Called when the user clicks "Save Changes" after editing a task.



6. update_task_list()

Purpose: Updates the task_listbox display to reflect the current state of the tasks list.

Functionality:

Clears the task_listbox.

Iterates over the tasks list, formatting each task with its title, category, and status (Completed/Pending).

Adds each formatted task string to the task_listbox.


Usage:

Called whenever the task list changes, such as after adding, editing, marking as completed, or deleting a task.



7. mark_task_completed()

Purpose: Marks a selected task as completed.

Functionality:

Checks if a task is selected in the task_listbox.

If a task is selected, updates its completed status to True.

Saves the updated list of tasks and refreshes the task display.

If no task is selected, displays a warning message.


Usage:

Called when the user clicks the "Mark as Completed" button.



8. delete_task()

Purpose: Deletes the selected task from the list.

Functionality:

Checks if a task is selected in the task_listbox.

If a task is selected, deletes it from the tasks list.

Saves the updated list of tasks and refreshes the task display.

If no task is selected, displays a warning message.


Usage:

Called when the user clicks the "Delete Task" button.



9. clear_entries()

Purpose: Clears the title, description, and category input fields.

Functionality:

Deletes any text currently in each of the three entry fields.


Usage:

Called after adding a task or saving changes to an edited task to reset the input fields for a new task.


