"""
68. Binary Tree Postorder Traversal
Easy
https://www.lintcode.com/problem/68

Given a binary tree, return the postorder traversal of its nodes' values.
"""
from typing import List
from tree_node import TreeNode


class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """

    def postorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = [root]
        postorder = []

        while stack:
            node = stack.pop()
            postorder.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return postorder[::-1]


if __name__ == "__main__":
    nodes = [1, 2, 3]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().postorder_traversal(tree)
    expected = [2, 3, 1]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nodes = [1, None, 2, 3]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().postorder_traversal(tree)
    expected = [3, 2, 1]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
