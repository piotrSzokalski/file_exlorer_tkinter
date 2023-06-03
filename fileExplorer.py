import datetime
import subprocess
import tkinter as tk
from tkinter import ttk
import os
import sys
import shutil

from file import File


class FileExplorer:
    def __init__(self) -> None:
        self.current_file_path = os.path.expanduser("~")
        self.button_list = []

        self.files = self.get_files(self.current_file_path)
        self.selected_files = []

        self.window = tk.Tk()
        self.window.title("Eksplorator plików")
        self.window.geometry("1000x800")

        self.frame = tk.Frame(self.window, bg="gray", bd=2, relief=tk.RAISED)
        self.frame.pack()

        self.window.bind("<FocusIn>", self.on_window_focused)

        # dropdown dysku
        self.drives = self.get_available_drives()

        self.selected_dive = tk.StringVar()

        self.selected_dive.set(self.drives[0])

        self.build_dropdown()

        # tabela z plikami

        self.treeview = ttk.Treeview(self.window, selectmode='extended')

        self.treeview["columns"] = ('Ikona', "Nazwa", "Rozmiar",
                                    "Data utworzenia", "Data modyfikacji")

    def on_window_focused(self, event):
        self.get_from_os_clipboard()
        # print('HERE')
        self.rebuild_table()

    # TODO
    def handle_select(self, event):
        # print("______________________________")
        selected_rows = self.treeview.selection()

        files = []

        for row in selected_rows:
            item_data = self.treeview.item(row)['values']
            file_path = os.path.join(self.current_file_path, item_data[1])
            if (os.path.exists(file_path)):
                files.append(File(file_path))

        self.selected_files = files

        # print("Selected:", selected_names)

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
        return sorted([File(os.path.join(directory, file_name)) for file_name in os.listdir(directory)], key=lambda file: file.get_name())

    def get_selected_file_paths(self):
        selected_record_names = [self.treeview.item(selection)["values"][1]
                                 for selection in self.treeview.selection()]
        # naprawka
        self.files = self.get_files(self.current_file_path)

        return [file.get_path(
        ) for file in self.files if file.get_name() in selected_record_names]

    def append_to_current_path(self, suffix: str):

        # self.current_file_path
        # new_file_path = self.current_file_path + suffix
        new_file_path = os.path.join(self.current_file_path, suffix)
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

    def table_row_to_file(self) -> File:
        is_folder, name, size, createion_data, modeyfication_date = self.treeview.item(
            self.treeview.focus())['values']

        print("________________________________________")
        print(self.treeview.item(self.treeview.focus())['values'])
        print("________________________________________")

        return File(os.path.join(self.current_file_path, name))

    def open_folder(self, file: File):
        path_before_opening = self.current_file_path
        try:
            self.append_to_current_path(file.get_name())
            self.rebuild_ui()
        except Exception as ex:
            print(f'Exception: {ex}')
            self.current_file_path = path_before_opening
            self.open_popup(f'Nie można otworzyć pliku \n {ex}')

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
        try:
            is_folder, name, size, createion_data, modeyfication_date = self.treeview.item(
                self.treeview.focus())['values']

            # chyba zbedne
            is_folder = True if is_folder == 'F' else False

            file = File(os.path.join(self.current_file_path, name))

            # print(file)

            if not file:
                return
            if file.is_folder():
                self.open_folder(file)
                return
            # Zrefaktorowac
            self.open_file(self.current_file_path + "//" + file.get_name())
        except:
            pass

    def can_paste_files(self) -> bool:
        try:
            data = self.window.clipboard_get()
            # print(f'in can_paste_files: \n {data}')
            return True
        except:
            return False

    def get_from_os_clipboard(self):
        try:
            data = self.window.clipboard_get()
            self.window.clipboard_clear()
            self.window.clipboard_append(data + '\n')
        except:
            pass

    def copy_files_paths_to_clipboard(self, paths):
        # print('Copping files')
        self.window.clipboard_clear()
        for path in paths:
            self.window.clipboard_append(path + '\n')
        self.window.update()
        # data = self.window.clipboard_get()
        # print(data)

    def cut_files(self):
        pass

    def pase_files(self):
        print('Pasting files:')
        file_paths = self.window.clipboard_get().split('\n')

        for file_path in file_paths:
            if not os.path.exists(file_path):
                continue

            # copied_file_new_path = file_path NIE NIE NIE

            copied_file_new_path = self.current_file_path

            file_name = os.path.split(file_path)[-1]
            # jesli obecnym folderze istnieje plik o takiej samej nazwie
            if os.path.exists(os.path.join(self.current_file_path, file_name)):

                copied_file_new_path = self.create_new_file_name(file_name)

                # print('noewa nazwa:  ' + copied_file_new_path)

            try:
                if os.path.isdir(file_path):
                    shutil.copytree(src=file_path,
                                    dst=copied_file_new_path,  dirs_exist_ok=True, copy_function=shutil.copy)
                else:
                    shutil.copy(src=file_path,
                                dst=copied_file_new_path)
            except Exception as ex:
                self.open_popup(f'Nie udało sie wkleić \n{ex}')

        self.rebuild_table()

    # Nowa nazwa aby uniknąć dwupłatowych nazw
    def create_new_file_name(self, file_name):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        try:
            file_name, file_extention = file_name.split('.')
            new_file_name = self.current_file_path + \
                "\\" + file_name + '(' + timestamp + ')' + '.' + file_extention
        except ValueError:
            new_file_name = self.current_file_path + \
                "\\" + file_name + '(' + timestamp + ')'

        return new_file_name

    def remove_files(self):
        for file in self.selected_files:
            if file.is_folder():
                self.delete_folder(file)
            else:
                self.delete_file(file)
        self.rebuild_table()

    def delete_folder(self, file: File) -> None:
        shutil.rmtree(file.path)

    def delete_file(self, file: File) -> None:
        os.remove(file.get_path())

    def rename_file(self, file_name):
        pass

    def create_folder(self, folder_name):
        folder_path = os.path.join(self.current_file_path, folder_name)
        if os.path.exists(folder_path):
            folder_name = self.create_new_file_name(folder_name)
            folder_path = os.path.join(self.current_file_path, folder_name)
        os.mkdir(folder_path)
        self.rebuild_table()

    def create_file(self, file_name):
        file_path = os.path.join(self.current_file_path, file_name)
        if os.path.exists(file_path):
            file_name = self.create_new_file_name(file_name)
            file_path = os.path.join(self.current_file_path, file_name)
        with open(file_path, 'w') as new_file:
            pass

        self.rebuild_table()

    def open_popup(self, text="Błąd"):
        print('here')
        popup = tk.Toplevel()
        popup.title("Popup Window")

        label = tk.Label(popup, text=text)
        label.pack(pady=10)

        button = tk.Button(popup, text="Close", command=popup.destroy)
        button.pack(pady=10)

    def build_dropdown(self):

        self.disk_dropdown = tk.OptionMenu(
            self.frame, self.selected_dive, *self.drives, command=self.change_drive)

        self.disk_dropdown.grid(row=0, column=0)

    def show_file_name_prompt_window(self, mode='create_file', title="Utwórz nowy plik"):
        prompt_window = tk.Toplevel(self.window)
        prompt_window.title(title)

        label = tk.Label(prompt_window, text=title)
        label.pack()
        entry = tk.Entry(prompt_window)
        entry.pack()

        def process_input():
            user_input = entry.get()
            prompt_window.destroy()
            prompt_actions = {
                'create_file': self.create_file,
                'create_folder': self.create_folder,
                'rename_file': self.rename_file,
            }
            prompt_actions[mode](user_input)

        ok_button = tk.Button(
            prompt_window, text="OK", command=process_input)
        ok_button.pack()

    def show_file_actions_menu(self, event):
        self.build_files_actions_menu().post(event.x_root, event.y_root)

    def build_files_actions_menu(self):
        actions_menu = tk.Menu(self.window, tearoff=False)

        selected_file_paths = self.get_selected_file_paths()

        # print(f'Building actions menu \n {selected_file_paths}')

        if len(selected_file_paths) == 0:
            actions_menu.add_command(
                label="Stwórz Folder", command=lambda: self.show_file_name_prompt_window(mode='create_folder', title='Stwórz folder'))
            actions_menu.add_command(
                label="Stwórz Plik", command=lambda: self.show_file_name_prompt_window(mode='create_file', title='Stwórz plik'))

            if self.can_paste_files():
                actions_menu.add_command(
                    label="Wklej", command=self.pase_files)
            return actions_menu

        if len(selected_file_paths) == 1:
            actions_menu.add_command(
                label="Zmień nazwę", command=lambda: self.show_file_name_prompt_window(mode='rename_file', title='Zmień nazwę'))

        actions_menu.add_command(
            label="Kopiuj", command=lambda paths=selected_file_paths: self.copy_files_paths_to_clipboard(paths))
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

            self.treeview.bind("<<TreeviewSelect>>", self.handle_select)

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
