import subprocess
import tkinter as tk
from tkinter import ttk
import os
import datetime


from file import File

# globals

current_file_path = os.path.expanduser("~")

button_list = []

# functions


def get_file_metadata(directory, file_name):
    file_path = os.path.join(directory, file_name)
    file_size = os.path.getsize(file_path)
    is_folder = os.path.isdir(file_path)
    creation_time = datetime.datetime.fromtimestamp(
        os.path.getctime(file_path))
    modification_time = datetime.datetime.fromtimestamp(
        os.path.getmtime(file_path))
    return (file_name, is_folder, file_size, creation_time, modification_time)


def get_files(directory: str):
    return [File(*get_file_metadata(directory, file_name))
            for file_name in os.listdir(directory)]


def append_to_current_path(suffix: str):

    global current_file_path
    new_file_path = current_file_path + suffix
    if os.path.exists(new_file_path):

        current_file_path = new_file_path
    return

# Zle


def detach_from_current_path(suffix: str):

    global current_file_path
    if current_file_path.split('\\')[-1] == suffix:
        return

    dirs = current_file_path.split('\\')

    new_file_path = current_file_path
    while new_file_path.split('\\')[-1] != suffix:
        new_file_path = '\\'.join(new_file_path.split('\\')[:-1])

    print(new_file_path)
    if os.path.exists(new_file_path):
        current_file_path = new_file_path
        rebuild_breadcrumb()
        rebuild_table()


def open_folder(file: File):
    append_to_current_path('\\' + file.get_name())
    rebuild_breadcrumb()
    rebuild_table()


def open_file(file_path: str):
    try:
        subprocess.run(['xdg-open', file_path])  # Linux
    except FileNotFoundError:
        try:
            subprocess.run(['open', file_path])  # macOS
        except FileNotFoundError:
            try:
                subprocess.run(['start', file_path], shell=True)  # Windows
            except FileNotFoundError:
                print("Failed to open the file.")


def handel_file_double_click(event, files):
    global current_file_path

    is_folder, name, size, createion_data, modeyfication_date = treeview.item(
        treeview.focus())['values']

    is_folder = True if is_folder == 'F' else False

    file = File(name, is_folder, size, createion_data, modeyfication_date)

    print(file)

    if not file:
        return
    if file.is_folder:
        open_folder(file)
        return
    open_file(current_file_path + "//" + file.get_name())


def build_breadcrumb(path):
    global button_list

    path_components = path.split("\\")
    current_path = ""

    for index, component in enumerate(path_components):

        current_path += component + "\\"
        button = ttk.Button(frame, text=component,
                            command=lambda path=current_path: detach_from_current_path(path.split('\\')[-2]))
        button_list.append(button)
        button.grid(row=0, column=index)


def rebuild_breadcrumb():
    global button_list
    global current_file_path

    for button in button_list:
        button.destroy()
    build_breadcrumb(current_file_path)


def build_table(files):
    # label1 = tk.Button(frame, text=current_file_path, width=300)
    # label1.pack()

    treeview.column("#0", width=0, stretch=tk.NO)
    treeview.column("Ikona",  width=50)
    treeview.column("Nazwa", stretch=tk.YES)
    treeview.column("Rozmiar", stretch=tk.YES)
    treeview.column("Data utworzenia", stretch=tk.YES)
    treeview.column("Data modyfikacji", stretch=tk.YES)

    treeview.heading("#0", text="", anchor=tk.W)
    treeview.heading("Ikona", text="Ikona", anchor=tk.W)
    treeview.heading("Nazwa", text="Nazwa", anchor=tk.W)
    treeview.heading("Rozmiar", text="Rozmiar", anchor=tk.W)
    treeview.heading("Data utworzenia", text="Data utworzenia", anchor=tk.W)
    treeview.heading("Data modyfikacji", text="Data modyfikacji", anchor=tk.W)

    for file in files:
        if file.get_name()[0] == '.':
            continue

        icon = 'F' if file.is_folder else 'P'
        treeview.insert(parent="", index="end",
                        values=(icon,) + file.get_data())
        treeview.bind(
            "<Double-1>", lambda event: handel_file_double_click(event, files))
    treeview.pack()


def rebuild_table():
    global treeview
    files = get_files(current_file_path)
    print(files)
    treeview.delete(*treeview.get_children())
    build_table(files)

# application


files = get_files(current_file_path)


window = tk.Tk()
window.title("Eksplorator plików")
window.geometry("800x500")

frame = tk.Frame(window, bg="gray", bd=2, relief=tk.RAISED)
frame.pack()


treeview = ttk.Treeview(window)


treeview["columns"] = ('Ikona', "Nazwa", "Rozmiar",
                       "Data utworzenia", "Data modyfikacji")

build_breadcrumb(current_file_path)
build_table(files)
window.mainloop()
