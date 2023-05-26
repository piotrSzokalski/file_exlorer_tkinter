import datetime
import os


class File:
    def __init__(self, file_path: str) -> None:

        self.path = file_path

        self._name = file_path.split("\\")[-1]
        self._is_folder = os.path.isdir(file_path)
        self._size = os.path.getsize(file_path)
        self._creation_time = datetime.datetime.fromtimestamp(
            os.path.getctime(file_path))
        self._modification_time = datetime.datetime.fromtimestamp(
            os.path.getmtime(file_path))

    def get_file_metadata(directory, file_name):
        file_path = os.path.join(directory, file_name)
        file_size = os.path.getsize(file_path)
        is_folder = os.path.isdir(file_path)
        creation_time = datetime.datetime.fromtimestamp(
            os.path.getctime(file_path))
        modification_time = datetime.datetime.fromtimestamp(
            os.path.getmtime(file_path))
        return (file_name, is_folder, file_size, creation_time, modification_time)

    def get_path(self) -> str:
        return self.get_path

    def get_name(self) -> str:
        return self._name

    def is_folder(self) -> bool:
        return self._is_folder

    def get_size(self) -> int:
        return self._size

    def get_creation_time(self):
        return self._creation_time

    def get_modification_time(self):
        return self._modification_time

    def __str__(self) -> str:
        return f"{self._name}\t {self._size} \t {self._creation_time}\t {self._modification_time}"

    def get_all_data(self):
        return (self._name, self._is_folder, self._size, self._creation_time, self._modification_time)

    def get_data(self):
        return (self._name, self._size, self._creation_time, self._modification_time)
