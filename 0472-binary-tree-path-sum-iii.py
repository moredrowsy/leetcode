"""
472. Binary Tree Path Sum III
Hard
https://www.lintcode.com/problem/472/

Give a binary tree, and a target number, find all path that the sum of nodes equal to target, the path could be start and end at any node in the tree.
"""
from tree_node import ParentTreeNode


"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum3(self, root, target):
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

    def dfs(self, root, target, paths):
        if root:
            path = []
            self.find_sum(root, None, target, paths, path)

            self.dfs(root.left, target, paths)
            self.dfs(root.right, target, paths)

    def find_sum(self, node, prev, target, paths, path):
        path.append(node.val)
        target -= node.val

        if target == 0:
            paths.append(path[:])

        if node.parent and node.parent is not prev:
            self.find_sum(node.parent, node, target, paths, path)

        if node.left and node.left is not prev:
            self.find_sum(node.left, node, target, paths, path)

        if node.right and node.right is not prev:
            self.find_sum(node.right, node, target, paths, path)

        path.pop()


if __name__ == "__main__":
    nodes = [1, 2, 3, 4]
    target = 6
    nodes = [ParentTreeNode(node) if node else None for node in nodes]
    tree = ParentTreeNode.get_parent_tree_from_treenode_list(nodes)
    output = Solution().binaryTreePathSum3(tree, target)
    expected = [[2, 4], [2, 1, 3], [3, 1, 2], [4, 2]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    nodes = [1, 2, 3, 4]
    target = 3
    nodes = [ParentTreeNode(node) if node else None for node in nodes]
    tree = ParentTreeNode.get_parent_tree_from_treenode_list(nodes)
    output = Solution().binaryTreePathSum3(tree, target)
    expected = [[1, 2], [2, 1], [3]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)
