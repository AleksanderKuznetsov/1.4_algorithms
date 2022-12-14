"""
linked list
"""


class Node:
    """
    Класс узла
    """
    def __init__(self, item: int):
        self.value = item  # Значение узла.
        self.next = None  # Связь. Следующий узел.


class LinkedList:
    """
    Класс связанного списка
    """
    def __init__(self):
        self.head = None  # Узел-голова списка.
        self.tail = None  # Завершающий узел

    def add_in_tail(self, item):
        """Добавить новый узел в конец спиcка"""
        # Если голова пустая - добавить в нее.
        # Если нет - назначить с помощью next значение в указатель на сл.узел.
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item  # Добавить в конец списка завершающий узел.

    def print_all_nodes(self):
        """Метод отладочного вывода списка"""
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val: int):
        """Найти нужный узел по заданному значению"""
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val: int) -> list:
        """
        Найти все узлы по заданному значению/
        :param val: Искомое значение
        :return: список узлов
        """
        array = []
        node = self.head
        while node is not None:
            if node.value == val:
                array.append(node)
            node = node.next
        return array

    def delete(self, val: int, all=False):
        """Удаление одного или нескольких узлов"""
        # Если список пустой, закончить:
        if self.head is None:
            return

        # Проверить заголовок. Если значение равно искомому, назначить следующее
        # значение заголовку
        while self.head.value == val:
            if self.head.next is None:  # Если один элемент всего, назначить tail'у None
                self.tail = None
            self.head = self.head.next
            # Если нужно удалить одно значение(False) или всего одно в списке (сл. = None):
            # закончить работу
            if all is False or self.head is None:
                return

        node = self.head
        while node.next is not None:
            # Если значение следующего узла равно искомому - назначить через одно.
            if node.next.value == val and all is False:  # Если нужно удалить один элемент
                node.next = node.next.next
                return
            if node.next.value == val and all is True:  # Если нужно удалить все элементы
                node.next = node.next.next
                self.tail = node  # Назначить хвост текущему узлу
                continue
            # Назначить текущему элементу следующий для сл. итерации цикла.
            node = node.next
            self.tail = node  # Назначить хвост текущему узлу
        return

    def clean(self):
        """
        Очистка всего списка
        :return: пусто
        """
        while self.head is not None:
            self.head = None
            # В tail записать None
            self.tail = None
        # return

    def len(self) -> int:
        """
        Метод вычисления текущей длины списка.
        :return: длина списка
        """
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        """
        Метод вставки узла newNode после заданного узла afterNode (из списка).
        Если afterNode = None добавить новый элемент первым в списке.
        :param afterNode: после этого элемента вставить.
        :param newNode: этот элемент вставить.
        """
        # Присвоить переменной новый узел
        new_node = Node(newNode)

        # Если список пустой.
        if self.head is None and afterNode is None:
            self.head = new_node
            self.tail = new_node
            return
        # Основная логика.
        node = self.head
        while node is not None:  # Цикл работает пока узел не пустой.
            if afterNode is None:  # Если нужно вставить первым узлом
                temp = self.head
                self.head = new_node
                self.head.next = temp
                break

            # Если значение последнее.
            if node.value == afterNode and node is self.tail:
                node.next = new_node
                self.tail = new_node
                break

            if node.value == afterNode:
                new_node.next = node.next
                node.next = new_node
                break
            node = node.next
        return
