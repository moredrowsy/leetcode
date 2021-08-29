"""
597. Subtree with Maximum Average
Easy
https://www.lintcode.com/problem/597/

Given a binary tree, find the subtree with maximum average. Return the root of the subtree.
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
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    max_avg = float('-inf')
    max_node = None

    def findSubtree2(self, root):
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        self.dfs(root, 0, 0)
        return self.max_node

    def dfs(self, node, sum_, count):
        if not node:
            return (0, 0)

        lsum, lcount = self.dfs(node.left, sum_, count)
        rsum, rcount = self.dfs(node.right, sum_, count)

        nsum = lsum + rsum + node.val
        ncount = lcount + rcount + 1

        avg = nsum/ncount
        if avg > self.max_avg:
            self.max_avg = avg
            self.max_node = node

        return (nsum, ncount)


if __name__ == "__main__":
    nodes = [1, -5, 11, 1, 2, 4, -2]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().findSubtree2(tree)
    expected = 11
    expected = TreeNode.find_node(tree, expected)
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nodes = [1, -5, 11]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().findSubtree2(tree)
    expected = 11
    expected = TreeNode.find_node(tree, expected)
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
