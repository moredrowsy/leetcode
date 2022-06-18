"""
94. Binary Tree Inorder Traversal
Easy
https://leetcode.com/problems/binary-tree-inorder-traversal/

Given the root of a binary tree, return the inorder traversal of its root' values.
"""
from typing import List, Optional
from tree_node import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        output = []
        self.inorder(root, output)
        return output

    def inorder(self, root, output):
        if root:
            self.inorder(root.left, output)
            output.append(root.val)
            self.inorder(root.right, output)


if __name__ == "__main__":
    root = [1, None, 2, 3]
    root = [TreeNode(node) if node else None for node in root]
    root = TreeNode.get_tree_from_treenode_list(root)
    output = Solution().inorderTraversal(root)
    expected = [1, 3, 2]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    root = []
    root = [TreeNode(node) if node else None for node in root]
    root = TreeNode.get_tree_from_treenode_list(root)
    output = Solution().inorderTraversal(root)
    expected = []
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    root = [1]
    root = [TreeNode(node) if node else None for node in root]
    root = TreeNode.get_tree_from_treenode_list(root)
    output = Solution().inorderTraversal(root)
    expected = [1]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
