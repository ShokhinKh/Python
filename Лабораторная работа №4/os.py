import os

# 1. Получение текущей рабочей директории
current_directory = os.getcwd()  # Получаем текущую рабочую директорию
print(f"Текущая рабочая директория: {current_directory}")

# 2. Список файлов и папок в текущей директории
files_and_dirs = os.listdir(current_directory)  # Получаем список файлов и папок
print("Содержимое текущей директории:")
for item in files_and_dirs:
    print(item)

# 3. Создание новой директории
new_directory = os.path.join(current_directory, "new_folder")  # Формируем путь новой директории
os.mkdir(new_directory)  # Создаем новую директорию
print(f"Создана новая директория: {new_directory}")

# 4. Переименование директории
renamed_directory = os.path.join(current_directory, "renamed_folder")  # Новый путь для переименования
os.rename(new_directory, renamed_directory)  # Переименовываем директорию
print(f"Директория переименована в: {renamed_directory}")

# 5. Удаление директории
os.rmdir(renamed_directory)  # Удаляем директорию
print(f"Удалена директория: {renamed_directory}")
