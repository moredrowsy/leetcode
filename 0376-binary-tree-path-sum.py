"""
376. Binary Tree Path Sum
Easy
https://www.lintcode.com/problem/376/

Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.

A valid path is from root node to any of the leaf nodes.
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
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        paths = []
        self.dfs(root, target, [], paths)
        return paths

    def dfs(self, node, target, path, paths):
        if not node:
            return

        path.append(node.val)
        target -= node.val

        if target == 0 and not node.left and not node.right:
            paths.append(path[:])

        self.dfs(node.left, target, path, paths)
        self.dfs(node.right, target, path, paths)

        path.pop()


if __name__ == "__main__":
    nodes = [1, 2, 4, 2, 3]
    target = 5
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().binaryTreePathSum(tree, target)
    expected = [[1, 2, 2], [1, 4]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    nodes = [1, 2, 4, 2, 3]
    target = 3
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().binaryTreePathSum(tree, target)
    expected = []

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)
