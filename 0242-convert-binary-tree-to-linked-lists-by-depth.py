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
    """
    @param {TreeNode} root the root of binary tree
    @return {ListNode[]} a lists of linked list
    """

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
            list_node = head = ListNode(0)

            for _ in range(size):
                node = queue.popleft()

                list_node.next = ListNode(node.val)
                list_node = list_node.next

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            lists.append(head.next)

        return lists


if __name__ == "__main__":
    nodes = [1, 2, 3, 4]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().binaryTreeToLists(tree)
    output_str = ListNode.print_list_node(output)
    expected = "1->null,2->3->null,4->null"
    print(f"\noutput\t\t{output_str}")
    print(f"expected\t{expected}")
    print(output_str == expected)

    nodes = []
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().binaryTreeToLists(tree)
    output_str = ListNode.print_list_node(output)
    expected = ""
    print(f"\noutput\t\t{output_str}")
    print(f"expected\t{expected}")
    print(output_str == expected)

    nodes = [1, None, 2, 3]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().binaryTreeToLists(tree)
    output_str = ListNode.print_list_node(output)
    expected = "1->null,2->null,3->null"
    print(f"\noutput\t\t{output_str}")
    print(f"expected\t{expected}")
    print(output_str == expected)
