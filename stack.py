from node import Node


class Stack:

    def __init__(self) -> None:
        self.base_node = Node('Base node')
        self.last = self.base_node

    def push(self, value) -> None:
        added_node = Node(value)

        if self.last is self.base_node:
            added_node.next_node = self.base_node
        else:
            added_node.next_node = self.last

        self.last = added_node

    def pop(self) -> Node:
        if self.last is not self.base_node:
            result = self.last
            self.last = self.last.next_node
            return result
        else:
            return None

    def empty(self) -> bool:
        return self.last is self.base_node
