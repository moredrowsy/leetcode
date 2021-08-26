"""TreeNode"""
from collections import deque


class TreeNode:

    @classmethod
    def get_tree_from_treenode_list(cls, treenodes):
        if not treenodes:
            return None

        queue = deque(treenodes)
        root = queue.popleft()
        roots = deque([root])

        while queue and roots:
            node = roots.popleft()
            if node:
                node.left = queue.popleft()
                node.right = queue.popleft() if queue else None

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

    def __eq__(self, o: object) -> bool:
        return self.val == o.val if o else False

    def insert(self, item):
        """Insert nodes by level from left to right"""
        queue = deque([self])

        if item and not isinstance(item, TreeNode):
            item = TreeNode(item)

        while queue:
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()

                if not node.left:
                    node.left = item
                    return
                if not node.right:
                    node.right = item
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


class ParentTreeNode(TreeNode):
    def __init__(self, val):
        super().__init__(val)
        self.parent = None

    @classmethod
    def get_parent_tree_from_treenode_list(cls, treenodes):
        queue = deque(treenodes)
        root = queue.popleft()
        roots = deque([root])

        while queue and roots:
            node = roots.popleft()
            node.left = queue.popleft()
            node.left.parent = node
            node.right = queue.popleft() if queue else None
            if node.right:
                node.right.parent = node

            roots.append(node.left)
            roots.append(node.right)

        return root
