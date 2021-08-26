"""
242. Convert Binary Tree to Linked Lists by Depth
Medium
https://www.lintcode.com/problem/242/

Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""
from list_node import ListNode
from tree_node import TreeNode
from collections import deque


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        if not root:
            return []

        lists = []
        queue = deque([root])

        while queue:
            size = len(queue)
            head = list_node = None

            for _ in range(size):
                node = queue.popleft()

                if list_node:
                    list_node.next = ListNode(node.val)
                    list_node = list_node.next
                else:
                    head = ListNode(node.val)
                    list_node = head

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            lists.append(head)

        return lists


def output_to_string(output):
    string = ""
    while output:
        list_node = output.pop(0)

        while list_node:
            string += str(list_node.val)
            list_node = list_node.next
            string += "->"

        string += "null,"
    string = string[:-1]
    return string


if __name__ == "__main__":
    nodes = [1, 2, 3, 4]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().binaryTreeToLists(tree)
    output_str = output_to_string(output)
    expected = "1->null,2->3->null,4->null"
    print(f"\noutput\t\t{output_str}")
    print(f"expected\t{expected}")
    print(output_str == expected)

    nodes = []
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().binaryTreeToLists(tree)
    output_str = output_to_string(output)
    expected = ""
    print(f"\noutput\t\t{output_str}")
    print(f"expected\t{expected}")
    print(output_str == expected)
