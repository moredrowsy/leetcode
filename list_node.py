class ListNode:
    @classmethod
    def print_list_node(cls, node):
        string = ""
        while node:
            list_node = node.pop(0)

            while list_node:
                string += str(list_node.val)
                list_node = list_node.next
                string += "->"

            string += "null,"
        string = string[:-1]
        return string

    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return f"{self.val}"

    def __str__(self) -> str:
        return f"{self.val}"

    def __eq__(self, o: object) -> bool:
        return self.val == o.val if o else False