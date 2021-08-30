"""
901. Closest Binary Search Tree Value II
Hard
https://www.lintcode.com/problem/901/

Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Constraints:
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

Challenge
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
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
    def closestKValues(self, root, target, k):
        """
        @param root: the given BST
        @param target: the given target
        @param k: the given k
        @return: k values in the BST that are closest to the target
        """
        return self.dfs(root, target, k)

    def dfs(self, root, target, k):
        """
        Using dict to map values.

        Time Complexity
        ---------------
        O(k + log n)

        Space Complexity
        ----------------
        O(k + log n)
        """
        values = []

        if not root or k == 0:
            return values

        lower_stack = self.get_stack(root, target)
        upper_stack = lower_stack[:]

        if target < lower_stack[-1].val:
            self.move_lower(lower_stack)
        else:
            self.move_upper(upper_stack)

        for _ in range(k):
            if not lower_stack or upper_stack and \
                    target - lower_stack[-1].val > upper_stack[-1].val - target:
                values.append(upper_stack[-1].val)
                self.move_upper(upper_stack)
            else:
                values.append(lower_stack[-1].val)
                self.move_lower(lower_stack)

        return values

    def get_stack(self, root, target):
        stack = []

        while root:
            stack.append(root)
            if target < root.val:
                root = root.left
            else:
                root = root.right

        return stack

    def move_lower(self, stack):
        node = stack[-1]

        if not node.left:
            node = stack.pop()
            while stack and stack[-1].left == node:
                node = stack.pop()
        else:
            node = node.left
            while node:
                stack.append(node)
                node = node.right

    def move_upper(self, stack):
        node = stack[-1]

        if not node.right:
            node = stack.pop()
            while stack and stack[-1].right == node:
                node = stack.pop()
        else:
            node = node.right
            while node:
                stack.append(node)
                node = node.left


if __name__ == "__main__":
    nodes = [1]
    target = 0.000000
    k = 1
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().closestKValues(tree, target, k)
    expected = [1]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    nodes = [3, 1, 4,  None, 2]
    target = 0.275000
    k = 2
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().closestKValues(tree, target, k)
    expected = [1, 2]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    nodes = [3, 1, 4,  None, 2]
    target = 0.275000
    k = 4
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().closestKValues(tree, target, k)
    expected = [1, 2, 3, 4]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    nodes = [2, 1, 3]
    target = 5.571429
    k = 2
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().closestKValues(tree, target, k)
    expected = [2, 3]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)
