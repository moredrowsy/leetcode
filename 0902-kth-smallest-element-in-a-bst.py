"""
902. Kth Smallest Element in a BST
Medium
https://www.lintcode.com/problem/902/

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Constraints:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
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
        self.k = 0
        self.kth_val = None

    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):
        self.dfs(root, k)
        return self.kth_val

    def dfs(self, root, k):
        """
        Using dict to map values.

        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        if not self.kth_val and root.left:
            self.dfs(root.left, k)

        self.k += 1

        if self.k == k:
            self.kth_val = root.val
            return

        if not self.kth_val and root.right:
            self.dfs(root.right, k)


if __name__ == "__main__":
    nodes = [1, None, 2]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    k = 2
    output = Solution().kthSmallest(tree, k)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nodes = [2, 1, 3]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    k = 1
    output = Solution().kthSmallest(tree, k)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
