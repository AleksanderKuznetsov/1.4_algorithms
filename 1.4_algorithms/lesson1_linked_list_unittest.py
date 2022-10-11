"""
Тестируем задание 1 - связанные списки
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

        # Проверка корректности создания списка.
        x = linked_array(s_list)
        self.assertTrue(x == [12, 12, 55, 55, 128, 128])

        # Удаление одного узла по значению.
        s_list.delete(12, False)
        x = linked_array(s_list)
        self.assertTrue(x == [12, 55, 55, 128, 128])

        # Удаление всех узлов по значению.
        s_list.delete(128, True)
        x = linked_array(s_list)
        self.assertTrue(x == [12, 55, 55])
        self.assertTrue(s_list.tail.value == 55)  # Проверка хвоста


        # Clean списка.
        s_list.clean()
        x = linked_array(s_list)
        self.assertTrue(x == [])
        self.assertTrue(s_list.head is None)  # Проверка головы
        self.assertTrue(s_list.tail is None)  # Проверка хвоста

        # Поиск всех узлов по конкретному значению.
        # Создать список.
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(55))
        s_list.add_in_tail(Node(55))
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(128))

        x = s_list.find_all(55)
        self.assertTrue(len(x) == 2)

        # Вычисление текущей длины списка.
        x = s_list.len()
        self.assertTrue(x == 6)

        # Вставка узла в середину
        s_list.insert(12, 63)
        x = linked_array(s_list)
        self.assertTrue(x == [12, 63, 12, 55, 55, 128, 128])

        # Вставка узла в начало.
        s_list.insert(None, 1)
        x = linked_array(s_list)
        self.assertTrue(x == [1, 12, 63, 12, 55, 55, 128, 128])

    def test_empty_list(self):
        """
        Тестирование пустого списка
        """
        # Создать список.
        s_list = LinkedList()

        # Проверка корректности создания списка.
        self.assertTrue(s_list.head is None)

        # Удаление одного узла по значению.
        s_list.delete(12, False)
        self.assertTrue(s_list.head is None)

        # Удаление всех узлов по значению.
        s_list.delete(55, True)
        self.assertTrue(s_list.head is None)

        # Clean списка.
        s_list.clean()
        self.assertTrue(s_list.head is None)  # Проверка головы
        self.assertTrue(s_list.tail is None)  # Проверка хвоста

        # Поиск всех узлов по конкретному значению.
        x = s_list.find_all(55)
        self.assertTrue(s_list.head is None)  # Проверка головы
        self.assertTrue(s_list.tail is None)  # Проверка хвоста

        # Вычисление текущей длины списка.
        x = s_list.len()
        self.assertTrue(x == 0)

        # Вставка узла в середину
        s_list.insert(12, 63)
        x = linked_array(s_list)
        self.assertTrue(x == [63])

        # Вставка узла в начало.
        s_list = LinkedList()  # перезапишем в пустой
        s_list.insert(None, 1)
        x = linked_array(s_list)
        self.assertTrue(x == [1])

    def test_one_element(self):
        """
        Тестирование одного элемента в списке
        """
        # Создать список.
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))

        # Проверка корректности создания списка.
        x = linked_array(s_list)
        self.assertTrue(x == [12])

        # Удаление одного узла по значению.
        s_list.delete(12, False)
        x = linked_array(s_list)
        self.assertTrue(x == [])

        # Удаление всех узлов по значению.
        s_list.add_in_tail(Node(12))
        s_list.delete(12, True)
        x = linked_array(s_list)
        self.assertTrue(x == [])

        # Clean списка.
        s_list.add_in_tail(Node(12))
        s_list.clean()
        self.assertTrue(s_list.head is None)

        # Поиск всех узлов по конкретному значению.
        s_list.add_in_tail(Node(12))
        x = s_list.find_all(12)
        self.assertTrue(len(x) == 1)

        # Вычисление текущей длины списка.
        x = s_list.len()
        self.assertTrue(x == 1)

        # Вставка узла в середину
        s_list.insert(12, 63)
        x = linked_array(s_list)
        self.assertTrue(x == [12, 63])

        # Вставка узла в начало.
        s_list = LinkedList()  # перезапишем в пустой
        s_list.add_in_tail(Node(12))
        s_list.insert(None, 1)
        x = linked_array(s_list)
        self.assertTrue(x == [1, 12])


if __name__ == '__main__':
    unittest.main()