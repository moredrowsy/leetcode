"""
246. Binary Tree Path Sum II
Medium
https://www.lintcode.com/problem/246/

Your are given a binary tree in which each node contains a value. Design an algorithm to get all paths which sum to a given value. The path can starts or ends at any node, but it must go in a straight line down.
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

    def binaryTreePathSum2(self, root, target):
        """
        Time Complexity
        ---------------
        O(n^2)

        Space Complexity
        ----------------
        O(n^2)
        """
        paths = []
        self.dfs(root, target, paths)
        return paths

    def dfs(self, node, target, paths):
        if not node:
            return

        self.find_sum(node, target, [], paths)
        self.dfs(node.left, target, paths)
        self.dfs(node.right, target, paths)

    def find_sum(self, node, target, path, paths):
        if not node:
            return

        path.append(node.val)
        target -= node.val

        if target == 0:
            paths.append(path[:])

        self.find_sum(node.left, target, path, paths)
        self.find_sum(node.right, target, path, paths)

        path.pop()


if __name__ == "__main__":
    nodes = [1, 2, 3, 4,  None, 2]
    target = 6
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().binaryTreePathSum2(tree, target)
    expected = [[2, 4], [1, 3, 2]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    nodes = [1, 2, 3, 4]
    target = 10
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().binaryTreePathSum2(tree, target)
    expected = []

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)
