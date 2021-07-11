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


def build_tree_node(values):
    from collections import deque
    val_queue = deque(values)
    root_node = TreeNode(val_queue.popleft())
    node_queue = deque([root_node])

    while val_queue:
        node = node_queue.popleft()
        node.left = TreeNode(val_queue.popleft())
        node.right = TreeNode(val_queue.popleft())

        node_queue.append(node.left)
        node_queue.append(node.right)

    return root_node


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
        self.min_val = float('inf')

    def findSubtree(self, root):
        self.getTreeSum(root)
        return self.min_root

    def getTreeSum(self, root):
        if root is None:
            return 0

        left_weight = self.getTreeSum(root.left)
        right_weight = self.getTreeSum(root.right)
        root_weight = left_weight + right_weight + root.val

        if root_weight < self.min_val:
            self.min_root = root
            self.min_val = root_weight

        return root_weight


if __name__ == "__main__":
    root = [1, -5, 2, 1, 2, -4, -5]
    root = build_tree_node(root)
    solution = Solution()
    answer = solution.findSubtree(root)
    print(answer)
