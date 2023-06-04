import datetime
import os


class File:
    def __init__(self, file_path: str) -> None:

        if file_path[2] != '\\':
            file_path = file_path[:2] + '\\' + file_path[2:]

        self.path = file_path

        self._name = file_path.split("\\")[-1]
        self._is_folder = os.path.isdir(file_path)
        self._size = os.path.getsize(file_path)
        self._creation_time = datetime.datetime.fromtimestamp(
            os.path.getctime(file_path))
        self._modification_time = datetime.datetime.fromtimestamp(
            os.path.getmtime(file_path))

    def get_path(self) -> str:
        return self.path

    def get_name(self) -> str:
        return self._name

    def get_extension(self) -> str:
        try:
            extension = self._name.split('.')[1]
            return extension
        except:
            return ''

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
        return (self._name, self._size, self._creation_time.strftime("%Y-%m-%d %H:%M:%S"), self._modification_time.strftime("%Y-%m-%d %H:%M:%S"))
