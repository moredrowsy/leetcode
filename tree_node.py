"""TreeNode"""
from collections import deque


class TreeNode:

    @classmethod
    def get_tree_from_treenode_list(cls, treenodes):
        queue = deque(treenodes)
        root = queue.popleft()
        roots = deque([root])

        while queue:
            node = roots.popleft()
            node.left = queue.popleft()
            node.right = queue.popleft()

            roots.append(node.left)
            roots.append(node.right)

        return root

    @classmethod
    def get_treenode_list_from_tree(cls, root):
        treenode_list = []
        queue = deque([root])
        rightmost_node = root.rightmost_node()

        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()

                treenode_list.append(node)

                if node is rightmost_node:
                    return treenode_list

                if node:
                    queue.append(node.left)
                    queue.append(node.right)

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

    def rightmost_node(self):
        return self._rightmost_node(self)

    def _rightmost_node(self, root):
        if root is None:
            return None

        right_node = self._rightmost_node(root.right)

        return right_node if right_node else root

    def get_queue(self):
        queue = []
        self._get_queue(self, queue)
        return queue

    def _get_queue(self, root, queue):
        queue.append(root)

        if root is None:
            return

        self._get_queue(root.left, queue)
        self._get_queue(root.right, queue)
