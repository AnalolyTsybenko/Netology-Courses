import unittest
from unittest.mock import patch
from Python_developer.Python_professional.F_Test_development.app \
    import documents, directories
from Python_developer.Python_professional.F_Test_development.app \
    import document_number_for_name, document_number_for_shelf_number, \
    show_all_documents, add_new_document_and_specify_a_shelf, delete_document


class TestFunction(unittest.TestCase):
    def test_document_number_for_name(self):
        with patch('builtins.input', return_value='2207 876234'):
            assert input() == '2207 876234'
            result = f'Этот документ человека по имени Василий Гупкин\n'
            self.assertMultiLineEqual(document_number_for_name(documents), result)

        with patch('builtins.input', return_value=''):
            assert input() == ''
            result = f'Номер документа не найден.\n'
            self.assertMultiLineEqual(document_number_for_name(documents), result)

    def test_document_number_for_shelf_number(self):
        with patch('builtins.input', return_value='2207 876234'):
            assert input() == '2207 876234'
            result = f'Номер полки: 1\n'
            self.assertMultiLineEqual(document_number_for_shelf_number(directories), result)

        with patch('builtins.input', return_value=''):
            assert input() == ''
            result = f'Номер документа не найден.\n'
            self.assertMultiLineEqual(document_number_for_shelf_number(directories), result)

    def test_show_all_documents(self):
        self.assertIsInstance(show_all_documents(documents), list)

    def test_add_new_document_and_specify_a_shelf(self):
        with patch('builtins.input', return_value='1'):
            assert input() == '1'
            result = f'Документ уже существует\n'
            new_document = {
                'type': 'passport',
                'number': '11-2',
                'name': 'Витайлий Паравозов'
            }
            self.assertMultiLineEqual(add_new_document_and_specify_a_shelf(
                documents, directories, new_document), result)

    def test_delete_document(self):
        with patch('builtins.input', return_value='11-2'):
            assert input() == '11-2'
            result = f'Документ удален.\n'
            self.assertMultiLineEqual(delete_document(documents, directories), result)
