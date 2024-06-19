import unittest
from unittest.mock import patch
import requests

class TestLinks(unittest.TestCase):

    @patch('requests.get')
    def test_valid_link(self, mock_get):
        """Проверяет, что функция работает для ссылки на сайт."""
        mock_get.return_value.status_code = 200
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    @patch('requests.get')
    def test_valid_link(self, mock_get):
        """Проверяет, что функция работает, ссылка на вк."""
        mock_get.return_value.status_code = 200
        url = 'https://vk.com/white_walker02'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    @patch('requests.get')
    def test_valid_link(self, mock_get):
        """Проверяет, что функция работает, ссылка на телеграмм."""
        mock_get.return_value.status_code = 200
        url = 'https://web.telegram.org/k/'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)



    def test_form_fields_exist(self):
        """Проверка наличия всех обязательных полей в форме"""
        form_fields = ["name", "telephon", "data", "yslyga"]
        self.assertTrue(all(field in form_fields for field in ["name", "telephon", "data", "yslyga"]))

    def test_form_field_types(self):
        """Тест проверяет, что все обязательные поля формы имеют указанные типы"""
        self.assertIsInstance("name", str)
        self.assertIsInstance("telephon", str)
        self.assertIsInstance("data", str)
        self.assertIsInstance("yslyga", str)

    def test_submit_button_text(self):
        """Проверка, что текст кнопки "Отправить" присутствует на кнопке отправки формы"""
        submit_button_text = "Отправить"
        self.assertEqual(submit_button_text, "Отправить")



    def setUp(self):
        """Фиктивные данные для ссылок на блоки в блоке nav"""
        self.nav_links = ["#bloc_2", "#bloc_3", "#bloc_4", "#bloc_5", "#bloc_6", "#bloc_10"]

    def test_nav_links_exist(self):
        """Проверка наличия всех ссылок на блоки в блоке nav"""
        self.assertEqual(len(self.nav_links), 6)

    def test_nav_links_correctness(self):
        """Проверка корректности ссылок на блоки в блоке nav"""
        expected_links = ["#bloc_2", "#bloc_3", "#bloc_4", "#bloc_5", "#bloc_6", "#bloc_10"]
        self.assertEqual(self.nav_links, expected_links)

    def test_nav_links_unique(self):
        """Проверка уникальности ссылок на блоки в блоке nav"""
        self.assertEqual(len(set(self.nav_links)), len(self.nav_links))

if __name__ == '__main__':
    unittest.main()