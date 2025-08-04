import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """Создание соединения с базой данных"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def execute_sql(conn, sql_command):
    """
    Выполнить SQL-команду
    :param conn: Соединение с базой данных
    :param sql_command: Команда SQL
    """
    try:
        c = conn.cursor()
        c.execute(sql_command)
    except Error as e:
        print(f'Ошибка при выполнении команды: {e}')


def create_table(conn, table_name, fields):
    """
    Создать таблицу в базе данных
    :param conn: соединение с базой данных
    :param table_name: имя таблицы
    :param fields: список полей и их типов данных
    """
    field_defs = ', '.join([f'{field_name} {data_type}' for field_name, data_type in fields.items()])
    sql_create_table = f"CREATE TABLE IF NOT EXISTS {table_name} ({field_defs});"
    if conn is not None:
        execute_sql(conn, sql_create_table)


def add_record(conn, table_name, values):
    """
    Добавить одну запись в таблицу
    :param conn: Соеденение с БД
    :param table_name: Имя таблицы
    :param values: Список значений для вставки
    """
    placeholders = ', '.join(['?'] * len(values))
    columns = ', '.join(values.keys())
    sql_insert = f'INSERT INTO {table_name}({columns}) VALUES({placeholders});'
    cursor = conn.cursor()
    cursor.execute(sql_insert, tuple(values.values()))
    conn.commit()  # Фиксируем изменения


def insert_multiple_records(conn, records, table):
    cursor = conn.cursor()

    # Получаем имена столбцов
    column_names = list(records[0].keys())
    question_marks = ', '.join('?' * len(column_names))

    query = f'''INSERT INTO {table} ({', '.join(column_names)}) VALUES ({question_marks})'''

    cursor.executemany(query, [tuple(record.values()) for record in records])
    conn.commit()  # Сохраняем изменения


def display_all_records(conn, table):
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM {table}')
    rows = cur.fetchall()
    for row in rows:
        print(row)


# Главная функция для запуска приложения
def main():
    database = r'schedule.db'

    conn = create_connection(database)

    with conn:
        # Меню приложения
        while True:
            print("\nМеню:")
            print("0. Завершить программу")
            print("1. Создать базу данных")
            print("2. Создать новую таблицу")
            print("3. Добавить запись в существующую таблицу")
            print("4. Добавить несколько записей в существующую таблицу")
            print("5. Вывести все записи из таблицы")
            choice = input("Введите номер пункта меню: ")

            if choice == '0':
                print("Завершение программы...")
                break

            elif choice == '1':
                # Создаем базу данных
                pass  # база данных уже создается при подключении

            elif choice == '2':
                table_name = input('Введите имя новой таблицы: ')
                if not table_name.isalnum():
                    print("Имя таблицы должно содержать только буквы и цифры. Повторите попытку.")
                    continue
                fields = {}
                n_fields = int(input('Сколько полей будет в таблице? '))
                for i in range(n_fields):
                    field_name = input(f'Введите название поля #{i + 1}: ')
                    if not field_name.isalnum():
                        print("Название поля должно содержать только буквы и цифры. Повторите попытку.")
                        continue
                    data_type = input(f"Введите тип данных для поля '{field_name}': ").upper()
                    if data_type not in ['INTEGER', 'REAL', 'TEXT', 'BLOB']:
                        print(
                            "Недопустимый тип данных. Допустимые варианты: INTEGER, REAL, TEXT, BLOB. Повторите попытку.")
                        continue
                    fields[field_name] = data_type

                create_table(conn, table_name, fields)
                print(f"Таблица '{table_name}' успешно создана.")

            elif choice == '3':
                table_name = input('\nВ какую таблицу добавить запись? ')
                if not table_exists(conn, table_name):
                    print(f"Таблица '{table_name}' не найдена. Убедитесь, что она была создана ранее.")
                    continue
                values = {}

                cur = conn.cursor()
                cur.execute(f"PRAGMA table_info('{table_name}')")  # Получим информацию о полях таблицы
                columns = [column[1] for column in cur.fetchall()]

                for col in columns:
                    value = input(f"Значение для поля {col}: ")
                    values[col] = value

                add_record(conn, table_name, values)
                print("Запись успешно добавлена!")

            elif choice == '4':
                table_name = input("\nВ какую таблицу вы хотите добавить несколько записей? ")
                if not table_exists(conn, table_name):
                    print(f"Таблица '{table_name}' не найдена. Убедитесь, что она была создана ранее.")
                    continue

                records = []
                num_records = int(input("Сколько записей вы хотите ввести? "))

                # Получаем информацию о колонках таблицы
                cur = conn.cursor()
                cur.execute(f"PRAGMA table_info('{table_name}')")
                columns = [info[1] for info in cur.fetchall()]

                print("\nДля каждой записи введите значения в следующем порядке:", ', '.join(columns))

                # Считываем данные для каждой записи
                for i in range(num_records):
                    record_dict = {}

                    for column in columns:
                        value = input(f"Введите значение для столбца '{column}': ")
                        record_dict[column] = value

                    records.append(record_dict)

                insert_multiple_records(conn, records, table=table_name)
                print("Все записи были успешно добавлены!")


            elif choice == '5':
                table_name = input('Какая таблица нужна для вывода? ')
                if not table_exists(conn, table_name):
                    print(f"Таблица '{table_name}' не найдена. Убедитесь, что она была создана ранее.")
                    continue
                display_all_records(conn, table_name)

            else:
                print("Неверный выбор. Попробуйте снова.")

        conn.commit()  # Фиксация всех изменений перед завершением работы
        print("Работа с базой данных завершена.")


def table_exists(conn, table_name):
    """Проверка существования таблицы в базе данных."""
    cur = conn.cursor()
    cur.execute(f"""SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table_name}'""")
    exists = cur.fetchone()[0]
    return bool(exists)


if __name__ == '__main__':
    main()



