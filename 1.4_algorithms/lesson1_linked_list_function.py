"""
Функция, которая получает на вход два связанных списка, состоящие из целых значений,
и если их длины равны, возвращает список, каждый элемент которого
равен сумме соответствующих элементов входных списков
"""

from lesson1_linked_list import *


def func(list1, list2):
    """
    :param list1: Связанный список 1
    :param list2: Связанный список 2
    :return: Результирующий третий список
    """
    # Посчитать длины списков
    list1_len = list1.len()
    list2_len = list2.len()

    # Закончить функцию, если длины не равны.
    if list1_len != list2_len:
        return None

    # Создать третий список
    result = LinkedList()

    node1 = list1.head
    node2 = list2.head
    while node1 is not None:
        temp = node1.value + node2.value
        result.add_in_tail(Node(temp))
        node1 = node1.next
        node2 = node2.next
    return result
