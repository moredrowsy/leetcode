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
    def closestValue(self, root, target):
        """
        @param root: the given BST
        @param target: the given target
        @return: the value in the BST that is closest to the target
        """
        return self.dfs_re(root, target)

    def dfs_iter(self, root, target):
        """
        Time Complexity
        ---------------
        O(log n)

        Space Complexity
        ----------------
        O(log n)
        """
        upper = root
        lower = root
        while root:
            if target > root.val:
                lower = root
                root = root.right
            elif target < root.val:
                upper = root
                root = root.left
            else:
                return root.val
        if abs(upper.val - target) <= abs(lower.val - target):
            return upper.val
        return lower.val

    def dfs_re(self, root, target):
        """
        Time Complexity
        ---------------
        O(log n)

        Space Complexity
        ----------------
        O(log n)
        """
        lower = self.lower_bound(root, target)
        upper = self.upper_bound(root, target)

        if not lower:
            return upper.val
        if not upper:
            return lower.val
        if abs(lower.val - target) < abs(upper.val - target):
            return lower.val
        return upper.val

    def lower_bound(self, root, target):
        if not root:
            return None

        if target < root.val:
            return self.lower_bound(root.left, target)

        lower = self.lower_bound(root.right, target)
        return lower if lower else root

    def upper_bound(self, root, target):
        if not root:
            return None

        if target >= root.val:
            return self.upper_bound(root.right, target)

        upper = self.upper_bound(root.left, target)
        return upper if upper else root


if __name__ == "__main__":
    nodes = [5, 4, 9, 2, None, 8, 10]
    target = 6.124780
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().closestValue(tree, target)
    expected = 5
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nodes = [3, 2, 4, 1]
    target = 4.142857
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().closestValue(tree, target)
    expected = 4
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nodes = [10, 5, 15, 3, 6, 12, 18, None, 4, None, 8]
    target = 4.142857
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().closestValue(tree, target)
    expected = 4
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
