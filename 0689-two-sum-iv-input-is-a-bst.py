"""
689.Two Sum IV - Input is a BST
Medium
https://www.lintcode.com/problem/689/

Given a binary search tree and a number n, find two numbers in the tree that sums up to n.
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
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, target):
        diff = set()
        pair = [None, None]
        self.dfs(root, target, diff, pair)
        return pair

    def dfs(self, root, target, diff, pair):
        if not root:
            return

        if root.val in diff:
            pair[0], pair[1] = root.val, target - root.val
            return

        diff.add(target - root.val)
        self.dfs(root.left, target, diff, pair)
        self.dfs(root.right, target, diff, pair)


if __name__ == "__main__":
    nodes = [4, 2, 5, 1, 3]
    target = 3
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().twoSum(tree, target)
    expected = [[1, 2], [2, 1]]

    status = False
    for e in expected:
        if e[0] == output[0] and e[1] == output[1]:
            status = True
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    nodes = [4, 2, 5, 1, 3]
    target = 5
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().twoSum(tree, target)
    expected = [[2, 3], [3, 2]]

    status = False
    for e in expected:
        if e[0] == output[0] and e[1] == output[1]:
            status = True
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)
