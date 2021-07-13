"""
596. Minimum Subtree
Easy
https://www.lintcode.com/problem/596/

Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.
The range of input and output data is in int.

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from tree_node import TreeNode


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def __init__(self) -> None:
        self.min_root = None
        self.min_sum = float('inf')

    def findSubtree(self, root):
        self.get_tree_sum(root)
        return self.min_root

    def get_tree_sum(self, root):
        if root is None:
            return 0

        left_sum = self.get_tree_sum(root.left)
        right_sum = self.get_tree_sum(root.right)
        root_sum = left_sum + right_sum + root.val

        if root_sum < self.min_sum:
            self.min_root = root
            self.min_sum = root_sum

        return root_sum


if __name__ == "__main__":
    nodes = [1, -5, 2, 1, 2, -4, -5]
    nodes = [TreeNode(node) for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    solution = Solution()
    answer = solution.findSubtree(tree)
    print(answer)
