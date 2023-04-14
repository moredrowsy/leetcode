"""
66. Binary Tree Preorder Traversal
Easy
https://www.lintcode.com/problem/66

Given a binary tree, return the preorder traversal of its nodes' values.
"""
from typing import List
from tree_node import TreeNode


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    def preorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()

            preorder.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return preorder


if __name__ == "__main__":
    nodes = [1, 2, 3]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().preorder_traversal(tree)
    expected = [1, 2, 3]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nodes = [1, None, 2, 3]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().preorder_traversal(tree)
    expected = [1, 2, 3]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
