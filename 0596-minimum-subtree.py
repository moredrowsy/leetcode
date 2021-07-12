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


def build_tree_from_tree_nodes(nodes):
    from collections import deque
    queue = deque(nodes)
    root = queue.popleft()
    roots = deque([root])

    while queue:
        node = roots.popleft()
        node.left = queue.popleft()
        node.right = queue.popleft()

        roots.append(node.left)
        roots.append(node.right)

    return root


class TreeNode:
    """Definition of TreeNode"""

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self) -> str:
        return f"{self.val}"


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
    root = build_tree_from_tree_nodes(nodes)
    solution = Solution()
    answer = solution.findSubtree(root)
    print(answer)
