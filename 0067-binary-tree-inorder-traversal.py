"""
67. Binary Tree Inorder Traversal
Easy
https://www.lintcode.com/problem/67

Given a binary tree, return the inorder traversal of its nodes' values.
"""
from typing import List
from tree_node import TreeNode


class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """

    def inorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        inorder = []
        while stack:
            node = stack.pop()

            if node.right:
                node = node.right

                while node:
                    stack.append(node)
                    node = node.left

            if stack:
                inorder.append(stack[-1].val)

        return inorder


if __name__ == "__main__":
    nodes = [1, 2, 3]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().inorder_traversal(tree)
    expected = [2, 1, 3]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nodes = [1, None, 2, 3]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().inorder_traversal(tree)
    expected = [1, 3, 2]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
