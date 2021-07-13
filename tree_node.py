"""TreeNode"""
from collections import deque


class TreeNode:

    @classmethod
    def build_tree_from_tree_nodes(cls, nodes):
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

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self) -> str:
        return f"{self.val}"

    def __str__(self) -> str:
        return f"{self.val}"

    def insert(self, val):
        """Insert nodes level from left to right"""
        queue = deque([self])

        while queue:
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()

                if not node.left:
                    node.left = TreeNode(val)
                    return
                if not node.right:
                    node.right = TreeNode(val)
                    return
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
