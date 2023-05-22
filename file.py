class File:
    def __init__(self, name: str, is_folder: bool, size: int, creation_time, modification_time) -> None:
        self.name = name
        self.is_folder = is_folder
        self.size = size
        self.creation_time = creation_time
        self.modification_time = modification_time

    def get_name(self) -> str:
        return self.name

    def is_folder(self) -> bool:
        return self.is_folder

    def get_size(self) -> int:
        return self.size

    def get_creation_time(self):
        return self.creation_time

    def get_modification_time(self):
        return self.modification_time

    def __str__(self) -> str:
        return f"{self.name}\t {self.size} \t {self.creation_time}\t {self.modification_time}"

    def get_all_data(self):
        return (self.name, self.is_folder, self.size, self.creation_time, self.modification_time)

    def get_data(self):
        return (self.name, self.size, self.creation_time, self.modification_time)
