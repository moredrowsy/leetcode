"""
900. Closest Binary Search Tree Value
Easy
https://www.lintcode.com/problem/900/

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Constraints:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
"""
from tree_node import TreeNode


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    def __init__(self) -> None:
        self.closest_node = None
        self.min_dist = float('inf')

    def closestValue(self, root, target):
        """
        @param root: the given BST
        @param target: the given target
        @return: the value in the BST that is closest to the target

        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        self.dfs(root, target)
        return self.closest_node.val

    def dfs(self, root, target):
        if not root:
            return

        dist = abs(root.val - target)
        if dist < self.min_dist:
            self.closest_node = root
            self.min_dist = dist

        self.dfs(root.left, target)
        self.dfs(root.right, target)


if __name__ == "__main__":
    nodes = [5, 4, 9, 2, None, 8, 10]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    target = 6.124780
    output = Solution().closestValue(tree, target)
    expected = 5
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nodes = [3, 2, 4, 1]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    target = 4.142857
    output = Solution().closestValue(tree, target)
    expected = 4
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
