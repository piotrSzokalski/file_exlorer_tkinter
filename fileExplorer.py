import subprocess
import tkinter as tk
from tkinter import ttk
import os
import sys

from file import File


class FileExplorer:
    def __init__(self) -> None:
        self.current_file_path = os.path.expanduser("~")
        self.button_list = []

        self.files = self.get_files(self.current_file_path)

        self.window = tk.Tk()
        self.window.title("Eksplorator plików")
        self.window.geometry("1000x800")

        self.frame = tk.Frame(self.window, bg="gray", bd=2, relief=tk.RAISED)
        self.frame.pack()

        # dropdown dysku
        self.drives = self.get_available_drives()

        self.selected_dive = tk.StringVar()

        self.selected_dive.set(self.drives[0])

        self.build_dropdown()

        # tabela z plikami

        self.treeview = ttk.Treeview(self.window, selectmode='extended')

        self.treeview["columns"] = ('Ikona', "Nazwa", "Rozmiar",
                                    "Data utworzenia", "Data modyfikacji")

    def run(self):
        self.build_breadcrumb(self.current_file_path)
        self.build_table(self.files)
        self.window.mainloop()

    def get_available_drives(self):
        drives = []
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            drive_path = letter + ':\\'
            if os.path.exists(drive_path):
                drives.append(drive_path)
        return drives

    def get_files(self, directory: str):
        return [File(os.path.join(directory, file_name)) for file_name in os.listdir(directory)]

    def get_selected_files(self):
        selected_record_names = [self.treeview.item(selection)["values"][1]
                                 for selection in self.treeview.selection()]
        selected_record_paths = [file.get_path(
        ) for file in self.files if file.get_name() in selected_record_names]
        print(selected_record_paths)

    def append_to_current_path(self, suffix: str):

        self.current_file_path
        new_file_path = self.current_file_path + suffix
        if os.path.exists(new_file_path):

            self.current_file_path = new_file_path
        return

    def detach_from_current_path(self, suffix: str):

        if self.current_file_path.split('\\')[-1] == suffix:
            return

        dirs = self.current_file_path.split('\\')

        new_file_path = self.current_file_path
        while new_file_path.split('\\')[-1] != suffix:
            new_file_path = '\\'.join(new_file_path.split('\\')[:-1])

        if os.path.exists(new_file_path):
            self.current_file_path = new_file_path
            self.rebuild_breadcrumb()
            self.rebuild_table()

    def open_folder(self, file: File):
        self.append_to_current_path('\\' + file.get_name())
        self.rebuild_ui()

    def open_file(self, file_path):
        try:
            if sys.platform == 'linux':
                subprocess.run(['xdg-open', file_path])
            elif sys.platform == 'darwin':
                subprocess.run(['open', file_path])
            elif sys.platform == 'win32':
                subprocess.run(
                    ['cmd', '/c', 'start', '', file_path], shell=True)
            else:
                raise OSError(f'Unsupported platform: {sys.platform}')
        except Exception as e:
            print(f'Error opening file: {e}')

    def change_drive(self, selection):
        if os.path.exists(selection):
            self.current_file_path = selection
            self.selected_dive.set(selection)

            self.rebuild_ui()
        else:
            print(f'wrong path {selection}')

    def handel_file_double_click(self):

        is_folder, name, size, createion_data, modeyfication_date = self.treeview.item(
            self.treeview.focus())['values']

        is_folder = True if is_folder == 'F' else False

        file = File(os.path.join(self.current_file_path, name))

        # print(file)

        if not file:
            return
        if file.is_folder():
            self.open_folder(file)
            return
        self.open_file(self.current_file_path + "//" + file.get_name())

    def copy_files(self):
        pass

    def cut_files(self):
        pass

    def remove_files(self):
        pass

    def build_dropdown(self):

        self.disk_dropdown = tk.OptionMenu(
            self.frame, self.selected_dive, *self.drives, command=self.change_drive)

        self.disk_dropdown.grid(row=0, column=0)

    def show_file_actions_menu(self, event):
        self.build_files_actions_menu().post(event.x_root, event.y_root)

    def build_files_actions_menu(self):
        actions_menu = tk.Menu(self.window, tearoff=False)
        # context_menu.add_command(label="Stwórz Folder", command=option1_callback)
        # context_menu.add_command(label="Stwórz Plik", command=option1_callback)
        # context_menu.add_command(label="Zmień nazwę", command=option1_callback)

        self.get_selected_files()

        actions_menu.add_command(label="Kopiuj", command=self.copy_files)
        actions_menu.add_command(label="Wytnij", command=self.cut_files)
        actions_menu.add_command(label="Usuń", command=self.remove_files)
        return actions_menu

    def build_breadcrumb(self, path):

        path_components = path.split("\\")[1:]
        current_path = ""

        self.build_dropdown()

        for index, component in enumerate(path_components):
            if component == '':
                continue

            current_path += component + "\\"
            button = ttk.Button(self.frame, text=component,
                                command=lambda path=current_path: self.detach_from_current_path(path.split('\\')[-2]))
            self.button_list.append(button)
            button.grid(row=0, column=index + 1)

    def build_table(self, files):

        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("Ikona",  width=50)
        self.treeview.column("Nazwa", stretch=tk.YES)
        self.treeview.column("Rozmiar", stretch=tk.YES)
        self.treeview.column("Data utworzenia", stretch=tk.YES)
        self.treeview.column("Data modyfikacji", stretch=tk.YES)

        self.treeview.heading("#0", text="", anchor=tk.W)
        self.treeview.heading("Ikona", text="Ikona", anchor=tk.W)
        self.treeview.heading("Nazwa", text="Nazwa", anchor=tk.W)
        self.treeview.heading("Rozmiar", text="Rozmiar", anchor=tk.W)
        self.treeview.heading("Data utworzenia",
                              text="Data utworzenia", anchor=tk.W)
        self.treeview.heading("Data modyfikacji",
                              text="Data modyfikacji", anchor=tk.W)

        for file in files:
            if file.get_name()[0] == '.':
                continue

            icon = 'F' if file.is_folder() else 'P'
            self.treeview.insert(parent="", index="end",
                                 values=(icon,) + file.get_data())
            self.treeview.bind(
                "<Double-1>", lambda event: self.handel_file_double_click())

            self.treeview.bind("<Button-3>", self.show_file_actions_menu)

        self.treeview.pack(fill=tk.BOTH, expand=True)

    def rebuild_breadcrumb(self):
        for button in self.button_list:
            button.destroy()
        self.build_breadcrumb(self.current_file_path)

    def rebuild_table(self):
        files = self.get_files(self.current_file_path)
        self.treeview.delete(*self.treeview.get_children())
        self.build_table(files)

    def rebuild_ui(self):
        self.rebuild_breadcrumb()
        self.rebuild_table()
