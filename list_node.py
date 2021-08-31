from typing import List


class ListNode:
    def __init__(self, x: int = 0, next=None):
        self.val = int(x)
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val}"

    def __str__(self) -> str:
        return f"{self.val}"

    def __eq__(self, o: object) -> bool:
        return self.val == o.val if o else False

    def __hash__(self) -> int:
        return id(self)

    @classmethod
    def print(cls, node):
        string = ""

        while node:
            string += str(node.val)
            node = node.next
            string += "->"

        string += "null,"

        return string[:-1]

    @classmethod
    def print_list_nodes(cls, nodes):
        string = ""
        for node in nodes:
            string += ListNode.print(node)
            string += ","
        return string[:-1]

    @classmethod
    def get_head_from_list(cls, values):
        list_node = dummy = ListNode()

        for val in values:
            list_node.next = ListNode(val)
            list_node = list_node.next

        return dummy.next
