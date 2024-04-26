from simple_term_menu import TerminalMenu

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class FileSystem:
    def __init__(self, total_space):
        self.total_space = total_space
        self.used_space = 0
        self.files = {}

    def create_file(self, name, size):
        if self.used_space + size > self.total_space:
            raise Exception("Not enough space")
        self.files[name] = File(name, size)
        self.used_space += size
        print(f"Файл {name} создан успешно.")

    def delete_file(self, name):
        if name in self.files:
            self.used_space -= self.files[name].size
            del self.files[name]
            print(f"Файл {name} удален успешно.")
        else:
            print(f"Файл {name} не найден.")

    def copy_file(self, source_name, dest_name):
        if source_name in self.files:
            source_file = self.files[source_name]
            self.create_file(dest_name, source_file.size)
        else:
            print(f"Файл {source_name} не найден.")

    def move_file(self, source_name, dest_name):
        if source_name in self.files:
            self.copy_file(source_name, dest_name)
            self.delete_file(source_name)
        else:
            print(f"Файл {source_name} не найден.")

    def rename_file(self, old_name, new_name):
        if old_name in self.files:
            file = self.files[old_name]
            self.files[new_name] = file
            del self.files[old_name]
            print(f"Файл {old_name} переименован в {new_name}.")
        else:
            print(f"Файл {old_name} не найден.")

def main():
    fs = FileSystem(64 * 1024)  # 64KB
    actions = ["Создать файл", "Удалить файл", "Копировать файл", "Переместить файл", "Переименовать файл", "Выйти"]
    terminal_menu = TerminalMenu(actions)

    while True:
        menu_entry_index = terminal_menu.show()

        if menu_entry_index == 0:
            name = input("Введите имя файла: ")
            size = int(input("Введите размер файла в байтах: "))
            fs.create_file(name, size)
        elif menu_entry_index == 1:
            name = input("Введите имя файла для удаления: ")
            fs.delete_file(name)
        elif menu_entry_index == 2:
            source_name = input("Введите имя исходного файла: ")
            dest_name = input("Введите имя нового файла: ")
            fs.copy_file(source_name, dest_name)
        elif menu_entry_index == 3:
            source_name = input("Введите имя файла для перемещения: ")
            dest_name = input("Введите новое имя файла: ")
            fs.move_file(source_name, dest_name)
        elif menu_entry_index == 4:
            old_name = input("Введите старое имя файла: ")
            new_name = input("Введите новое имя файла: ")
            fs.rename_file(old_name, new_name)
        elif menu_entry_index == 5:
            print("Выход из программы.")
            break

if __name__ == "__main__":
    main()
