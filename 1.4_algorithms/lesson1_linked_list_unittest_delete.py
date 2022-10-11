"""
Тестируем задание 1 - удаление нескольких элементов разом
"""

import unittest
from lesson1_linked_list import *


def linked_array(linked_list) -> list:
    """
    Складываем значения списка в массив для проверки
    :param linked_list: связанный список
    :return: массив значений
    """
    array = []
    node = linked_list.head
    while node is not None:
        array.append(node.value)
        node = node.next
    return array


class TestWork(unittest.TestCase):
    """
    Тестирование задания 1 - связанные списки
    """

    def test_normal_result(self):
        """
        Тестирование нормальных условий
        """
        # Создать список.
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(55))
        s_list.add_in_tail(Node(55))
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(128))

        # Удаление одного узла по значению.
        s_list.delete(12, False)
        x = linked_array(s_list)
        self.assertTrue(x == [12, 55, 55, 128, 128])
        self.assertTrue(s_list.head.value == 12)  # Проверка заголовка
        self.assertTrue(s_list.tail.value == 128)  # Проверка хвоста

        # Удаление всех узлов по значению в конце списка.
        s_list.delete(128, True)
        x = linked_array(s_list)
        self.assertTrue(x == [12, 55, 55])
        self.assertTrue(s_list.head.value == 12)  # Проверка заголовка
        self.assertTrue(s_list.tail.value == 55)  # Проверка хвоста

        # Удаление всех узлов по значению в середине списка.
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(55))
        s_list.add_in_tail(Node(55))
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(128))

        s_list.delete(55, True)
        x = linked_array(s_list)
        self.assertTrue(x == [12, 12, 128, 128])
        self.assertTrue(s_list.head.value == 12)  # Проверка заголовка
        self.assertTrue(s_list.tail.value == 128)  # Проверка хвоста

    def test_empty_list(self):
        """
        Тестирование пустого списка
        """
        # Создать список.
        s_list = LinkedList()

        # Удаление одного узла по значению.
        s_list.delete(12, False)
        self.assertTrue(s_list.head is None)

        # Удаление всех узлов по значению.
        s_list.delete(55, True)
        self.assertTrue(s_list.head is None)

    def test_one_element(self):
        """
        Тестирование одного элемента в списке
        """
        # Создать список.
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))

        # Удаление одного узла по значению.
        s_list.delete(12, False)
        x = linked_array(s_list)
        self.assertTrue(x == [])

        # Удаление всех узлов по значению.
        s_list.add_in_tail(Node(12))
        s_list.delete(12, True)
        x = linked_array(s_list)
        self.assertTrue(x == [])


if __name__ == '__main__':
    unittest.main()
# -- coding: utf-8 --ИЛИ
