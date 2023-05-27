import tkinter as tk
from tkinter import ttk


def navigate_to(path):
    # Implement your logic to navigate to the specified path
    print("Navigating to:", path)


def create_breadcrumb(path):
    window = tk.Tk()

    # Split the path into individual components
    path_components = path.split("/")
    current_path = ""

    # Create buttons for each path component
    for index, component in enumerate(path_components):
        current_path += component + "/"
        button = ttk.Button(window, text=component,
                            command=lambda path=current_path: navigate_to(path))
        button.grid(row=0, column=index)

    window.mainloop()


# Example usage
file_path = "/home/user/documents/filename.txt"
create_breadcrumb(file_path)
