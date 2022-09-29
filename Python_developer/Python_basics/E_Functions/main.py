# Task_1_and_2

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def document_number_for_name():
    """Gets document number returns name"""

    document_number = input('Введите номер документа: ')
    for number in documents:
        if number['number'] == document_number:
            return print(f'Этот документ человека по имени {number["name"]}.')
    else:
        print('Номер документа не найден.')


def document_number_for_shelf_number():
    """Gets document number returns shelf number"""

    document_number = input('Введите номер документа: ')
    for shelf_number in directories:
        if document_number in directories[shelf_number]:
            return print(f'Номер полки: {shelf_number}.')
    else:
        print('Номер документа не найден.')


def show_all_documents():
    """Output of all documents in the specified format"""

    for value in documents:
        print(f'{value["type"]} "{value["number"]}" "{value["name"]}"')


def add_new_document_and_specify_a_shelf():
    """Accepts data for a new document and asks which shelf to put on"""

    type_document = input('Введите тип документа: ')
    number_document = input('Введите номер документа: ')
    document_owner_name = input('Введите имя владельца документа: ')
    shelf_number = input('Введите номер полки: ')

    document = {
        "type": type_document,
        "number": number_document,
        "name": document_owner_name
    }

    for number_shelf in directories:
        if number_shelf == shelf_number:
            directories[shelf_number] += [number_document]
            documents.append(document)
            return print('Документ добавлен.')
    else:
        print('Номер полки не найден, документ не добавлен.')


def delete_document():
    """Gets the document number and removes the document and its number from the shelf"""

    document_number = input('Введите номер документа: ')
    for number in documents:
        if number['number'] == document_number:
            documents.remove(number)

    for list_value in directories.values():
        for doc_number in list_value:
            if doc_number == document_number:
                list_value.remove(document_number)
                return print('Документ удален.')
    else:
        print('Номер документа не найден.')


def moving_a_document_to_a_new_shelf():
    """Gets the document number and new shelf number, moves the document from the current shelf to the new one"""

    document_number = input('Введите номер документа: ')
    for number in directories.values():
        if document_number in number:
            new_shelf_number = input('Введите номер новой полки: ')
            if new_shelf_number not in directories.keys():
                return print(f'Полка №{new_shelf_number} не найдена.')
            number.remove(document_number)
            current_list = directories[new_shelf_number]
            current_list.append(document_number)
            return print(f'Документ {document_number} перенесен на полку №{new_shelf_number}')
    return print(f'Документ {document_number} не найден.')


def add_new_shelf_number():
    """Gets the shelf number and creates it in the catalog"""

    new_shelf_number = input('Введите номер новой полки: ')
    for shelf_number in directories:
        if new_shelf_number == shelf_number:
            return print(f'Полка №{new_shelf_number} уже есть.')

    new_shelf = {new_shelf_number: []}
    directories.update(new_shelf)
    print(f'Полка №{new_shelf_number} создана.')


def help_menu():
    """Shows a menu with a set of commands"""

    print("""
    Помощь:
    * 'p' - По номеру документа показать имя владельца.
    * 's' - По номеру документа показать на какой полке он лежит.
    * 'l' - Вывод всех документов.
    * 'a' - Добавление нового документа с указанием полки.
    * 'd' - Удаление документа по его номеру.
    * 'm' - Перемещение документа по его номеру с указанием новой полки.
    * 'as' - Добавление новой полки.
    * 'h' - Помощь.
    * 'q' - Выход.
    """)


def main():
    """Command menu"""

    help_menu()

    while True:
        command = input('\nВведите команду: ')
        if command == 'p':
            document_number_for_name()
        elif command == 's':
            document_number_for_shelf_number()
        elif command == 'l':
            show_all_documents()
        elif command == 'a':
            add_new_document_and_specify_a_shelf()
        elif command == 'd':
            delete_document()
        elif command == 'm':
            moving_a_document_to_a_new_shelf()
        elif command == 'as':
            add_new_shelf_number()
        elif command == 'h':
            help_menu()
        elif command == 'q':
            print('Выход - программа завершена.')
            break
        else:
            print('Команда не найдена - программа завершена.')
            break


main()
