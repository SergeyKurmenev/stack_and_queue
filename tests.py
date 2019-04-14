import unittest
from my_queue import MyQueue
from stack import Stack
from node import Node


class TestMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.test_stack = Stack()
        self.test_queue = MyQueue()
        self.test_array = []

    def test_stack(self):
        # проверяю, что создаётся пустым
        self.assertTrue(self.test_stack.empty())

        # добавляю 100 элементов - после каждого добавления проверяю empty
        # - должен возвращать false - т.к. элементы добавляются
        for x in range(100):
            self.test_stack.push(x)
            self.assertFalse(self.test_stack.empty())

        # переопределил __eq__ в Node для сравнения только значений
        # извлекаю 99 значений, создавая для каждого Node с ожидаемым значением и сравниваю их
        for x in range(99, 0, -1):
            equals_node = Node(x)
            self.assertEqual(self.test_stack.pop(), equals_node)

        # проверяю, что стек не пустой. Затем достаю последний Node и проверяю ещё раз
        self.assertFalse(self.test_stack.empty())
        self.test_stack.pop()
        self.assertTrue(self.test_stack.empty())

        # проверяю, что пустой стэк при попытки достать элемент - возвращает None
        self.assertIsNone(self.test_stack.pop())

    def test_my_queue(self):
        # делаю такие же проверки, как для стека

        # проверяю, что создаётся пустым
        self.assertTrue(self.test_queue.empty())

        # добавляю 100 элементов - после каждого добавления проверяю empty
        # - должен возвращать false - т.к. элементы добавляются
        for x in range(100):
            self.test_queue.enqueue(x)
            self.assertFalse(self.test_queue.empty())

        # извлекаю 99 значений, создавая для каждого Node с ожидаемым значением и сравниваю их
        for x in range(99):
            equals_node = Node(x)
            self.assertEqual(self.test_queue.dequeue(), equals_node)

        # проверяю, что стек не пустой. Затем достаю последний Node и проверяю ещё раз
        self.assertFalse(self.test_queue.empty())
        self.test_queue.dequeue()
        self.assertTrue(self.test_queue.empty())

        # проверяю, что пустой стэк при попытки достать элемент - возвращает None
        self.assertIsNone(self.test_queue.dequeue())


if __name__ == '__main__':
    unittest.main()
