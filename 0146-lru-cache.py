"""
146. LRU Cache
Medium
https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
 - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
 - int get(int key) Return the value of the key if the key exists, otherwise return -1.
 - void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""
from collections import deque


class CacheItem:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val

    def __repr__(self) -> str:
        return f"{self.key}:{self.val}"


class DoublyLinkedNode:
    def __init__(self, item) -> None:
        self.item = item
        self.prev = None
        self.next = None

    def __repr__(self) -> str:
        return f"{self.item}"


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        items = []
        node = self.head
        while node:
            items.append(node.item)
            node = node.next
        return f"{items}"

    def insert_front(self, item):
        node = item if isinstance(
            item, DoublyLinkedNode) else DoublyLinkedNode(item)

        if not self.head:
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        node.prev = None

        if not self.tail:
            self.tail = node

    def insert_back(self, item):
        node = item if isinstance(
            item, DoublyLinkedNode) else DoublyLinkedNode(item)

        if not self.tail:
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        node.next = None

        if not self.head:
            self.head = node

    def remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        if self.head is node:
            self.head = node.next
        if self.tail is node:
            self.tail = node.prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.nodes = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self.nodes.remove_node(node)
        self.nodes.insert_back(node)
        return node.item.val

    def put(self, key: int, value: int) -> None:

        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.nodes.remove_node(node)
            self.nodes.insert_back(node)
            node.item.val = value
        else:
            node = DoublyLinkedNode(CacheItem(key, value))
            self.nodes.insert_back(node)
            self.key_to_node[key] = node

        # Remove front (least recently used) if over capacity
        n = len(self.key_to_node)
        if n > self.capacity:
            del self.key_to_node[self.nodes.head.item.key]
            self.nodes.remove_node(self.nodes.head)


class LRUCache2:
    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)

        if len(self.cache) > self.capacity:
            front = next(iter(self.cache))
            del self.cache[front]


def process_problem(cmds, args):
    output = []
    cache = None
    for cmd, arg in zip(cmds, args):
        result = None

        if cmd == "LRUCache":
            cache = LRUCache2(arg[0])
        elif cmd == "get":
            result = cache.get(arg[0])
        elif cmd == "put":
            result = cache.put(arg[0], arg[1])

        output.append(result)

    return output


if __name__ == "__main__":
    cmds = ["LRUCache", "put", "put", "get",
            "put", "get", "put", "get", "get", "get"]
    args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    output = process_problem(cmds, args)
    expected = [None, None, None, 1, None, -1, None, -1, 3, 4]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    cmds = ["LRUCache", "get", "put", "get", "put", "put", "get", "get"]
    args = [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]
    output = process_problem(cmds, args)
    expected = [None, -1, None, -1, None, None, 2, 6]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
