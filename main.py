import tkinter as tk
from tkinter import ttk
import os
import datetime


from file import File

# globals

current_file_path = os.path.expanduser("~")

print(current_file_path)

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


# application

files = get_files(current_file_path)


window = tk.Tk()
window.title("Eksplorator plików")
window.geometry("800x500")

frame = tk.Frame(window, bg="gray", bd=2, relief=tk.RAISED)
frame.pack()


label1 = tk.Button(frame, text='Scieżka')
label1.pack()


treeview = ttk.Treeview(window)


treeview["columns"] = ('Ikona', "Nazwa", "Rozmiar",
                       "Data utworzenia", "Data modyfikacji")


treeview.column("#0", width=0, stretch=tk.NO)
treeview.column("Ikona", stretch=tk.YES)
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
    # if (file.get_name()[0] == '.'):
    # continue

    treeview.insert(parent="", index="end",
                    values=('ikona',) + file.get_data())
    # treeview.insert(parent="", index="end", values=(1, 2, 3, 4))

treeview.pack()

window.mainloop()
