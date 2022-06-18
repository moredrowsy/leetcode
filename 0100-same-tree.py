"""
100. Same Tree
Easy
https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""
from typing import List, Optional
from tree_node import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(1)
        """
        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False
        if p.val != q.val:
            return False

        isSame = self.isSameTree(p.left, q.left)

        if not isSame:
            return False

        return self.isSameTree(p.right, q.right) and isSame


if __name__ == "__main__":
    p, q = [1, 2, 3], [1, 2, 3]
    p = [TreeNode(node) if node else None for node in p]
    q = [TreeNode(node) if node else None for node in q]
    p = TreeNode.get_tree_from_treenode_list(p)
    q = TreeNode.get_tree_from_treenode_list(q)
    output = Solution().isSameTree(p, q)
    expected = True
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    p, q = [1, 2], [1, None, 2]
    p = [TreeNode(node) if node else None for node in p]
    q = [TreeNode(node) if node else None for node in q]
    p = TreeNode.get_tree_from_treenode_list(p)
    q = TreeNode.get_tree_from_treenode_list(q)
    output = Solution().isSameTree(p, q)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    p, q = [1, 2, 1], [1, 1, 2]
    p = [TreeNode(node) if node else None for node in p]
    q = [TreeNode(node) if node else None for node in q]
    p = TreeNode.get_tree_from_treenode_list(p)
    q = TreeNode.get_tree_from_treenode_list(q)
    output = Solution().isSameTree(p, q)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    p, q = [10, 5, 15], [10, 5, None, None, 15]
    p = [TreeNode(node) if node else None for node in p]
    q = [TreeNode(node) if node else None for node in q]
    p = TreeNode.get_tree_from_treenode_list(p)
    q = TreeNode.get_tree_from_treenode_list(q)
    output = Solution().isSameTree(p, q)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
