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


def document_number_for_name(docs):
    """Gets document number returns name"""

    doc_num = input('Введите номер документа: ')
    for num in docs:
        if num['number'] == doc_num:
            return f'Этот документ человека по имени {num["name"]}\n'
    return 'Номер документа не найден.\n'


def document_number_for_shelf_number(dirs):
    """Gets document number returns shelf number"""

    doc_num = input('Введите номер документа: ')
    for key, value in dirs.items():
        if doc_num in value:
            return f'Номер полки: {key}\n'
    return 'Номер документа не найден.\n'


def show_all_documents(docs):
    """Output of all documents in the specified format"""

    user_list = []
    for doc in docs:
        user_list.append(list(doc.values()))
    return user_list


def new_document_for_add(doc_type, doc_number, doc_owner):
    """Add dictionary"""

    new_document = {
        'type': doc_type,
        'number': doc_number,
        'name': doc_owner
    }
    return new_document


def add_new_document_and_specify_a_shelf(docs, dirs, new_doc):
    """Accepts data for a new document and asks which shelf to put on"""

    shelf_num = input('Введите номер полки: ')
    for num in docs:
        if num['number'] == new_doc['number']:
            return f'Документ уже существует\n'
    if shelf_num in dirs.keys():
        docs.append(new_doc)
        dirs[shelf_num].append(new_doc['number'])
        return 'Документ добавлен.\n'
    return 'Номер полки не найден.\n'


def delete_document(docs, dirs):
    """Gets the document number and removes the document and its number from the shelf"""

    num_doc = input('Введите номер документа: ')
    if any(num_doc in shelf for shelf in dirs.values()):
        for key in dirs.keys():
            if num_doc in dirs[key]:
                dirs[key].remove(num_doc)
        for doc in docs:
            if doc['number'] == num_doc:
                docs.remove(doc)
        return 'Документ удален.\n'
    return 'Номер документа не найден.\n'


def moving_a_document_to_a_new_shelf(docs, dirs):
    """Gets the document number and new shelf number, moves the document from the current shelf to the new one"""

    num_doc = input('Введите номер документа: ')
    num_shelf = input('Введите номер новой полки: ')
    if num_shelf not in dirs.keys():
        return f'Полка №{num_shelf} не найдена.\n'
    elif not any(num_doc in shelf for shelf in dirs.values()):
        return f'Документ {num_doc} не найден.\n'
    else:
        for key in dirs.keys():
            if num_doc in dirs[key]:
                dirs[key].remove(num_doc)
                dirs[num_shelf].append(num_doc)
        return 'Документ перенесен на указанную полку.\n'


def add_new_shelf_number(dirs):
    """Gets the shelf number and creates it in the catalog"""

    num_shelf = input('Введите номер новой полки: ')
    if num_shelf not in dirs.keys():
        dirs.setdefault(num_shelf, [])
        return 'Полка создана.\n'
    else:
        return 'Полка уже есть.\n'


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
        command = input('Введите команду: ')
        if command == 'p':
            print(f'\n{document_number_for_name(documents)}')
        elif command == 's':
            print(f'\n{document_number_for_shelf_number(directories)}')
        elif command == 'l':
            print(show_all_documents(documents))
        elif command == 'a':
            type_ = input('Введите тип документа: ')
            number = input('Введите номер документа: ')
            name = input('Введите имя владельца документа: ')
            new_doc = new_document_for_add(type_, number, name)
            print(f'\n{add_new_document_and_specify_a_shelf(documents, directories, new_doc)}')
        elif command == 'd':
            print(f'\n{delete_document(documents, directories)}')
        elif command == 'm':
            print(f'\n{moving_a_document_to_a_new_shelf(documents, directories)}')
        elif command == 'as':
            print(f'\n{add_new_shelf_number(directories)}')
        elif command == 'h':
            help_menu()
        elif command == 'q':
            return 'Выход'


if __name__ == '__main__':
    main()
