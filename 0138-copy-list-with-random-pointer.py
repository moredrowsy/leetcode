"""
138. Copy List with Random Pointer
Medium
https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or None.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or None if it does not point to any node.
Your code will only be given the head of the original linked list.

Constraints:

0 <= n <= 1000
-10000 <= Node.val <= 10000
Node.random is None or is pointing to some node in the linked list.
"""
from node import Node

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        Using dict to map values.

        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        nodes_map = {}
        new_node = dummy = Node(0)

        # Copy linked list
        node = head
        while node:
            clone = Node(node.val)
            clone.random = node.random
            nodes_map[node] = clone

            new_node.next = clone
            new_node = new_node.next
            node = node.next

        # Assign random to new nodes
        new_node = dummy.next
        while new_node:
            if new_node.random:
                new_node.random = nodes_map[new_node.random]
            new_node = new_node.next

        return dummy.next


def input_to_head(nodes):
    node_list = [Node(node[0]) for node in nodes]
    head = Node(0)
    tmp = head

    for i, node in enumerate(nodes):
        _, index = node

        tmp.next = node_list[i]

        if index is not None and index < len(node_list):
            tmp.next.random = node_list[index]

        tmp = tmp.next

    return head.next


if __name__ == "__main__":
    input_nodes = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head = input_to_head(input_nodes)
    output = Solution().copyRandomList(head)

    status = True
    node = head

    try:
        while node:
            if node.val != output.val or node is output:
                status = False
                break

            if node.random and (node.random is output.random or node.random.val != output.random.val):
                status = False
                break

            node = node.next
            output = output.next
    except:
        status = False

    print(status)
    input_nodes = [[3, None], [3, 0], [3, None]]
    head = input_to_head(input_nodes)
    output = Solution().copyRandomList(head)

    status = True
    node = head

    try:
        while node:
            if node.val != output.val or node is output:
                status = False
                break

            if node.random and (node.random is output.random or node.random.val != output.random.val):
                status = False
                break

            node = node.next
            output = output.next
    except:
        status = False

    print(status)
