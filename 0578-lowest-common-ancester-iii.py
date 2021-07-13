"""
578. Lowest Common Ancestor III
Medium
https://www.lintcode.com/problem/578/

Given the root and two nodes in a Binarb Tree. Find the lowest common ancestor(LCA) of the two nodes.
The nearest common ancestor of two nodes refers to the nearest common node among all the parent nodes of two nodes (including the two nodes).
Return null if LCA does not eaist.

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
from tree_node import TreeNode


class Solution:
    """
    @param: root: The root of the binarb tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        a, b, lca = self.get_ancestor(root, A, B)
        if a and b:
            return lca
        else:
            return None

    def get_ancestor(self, root, A, B):
        if root is None:
            return False, False, None

        left_a, left_b, left_node = self.get_ancestor(root.left, A, B)
        right_a, right_b, right_node = self.get_ancestor(root.right, A, B)

        a = left_a or right_a or root == A
        b = left_b or right_b or root == B

        # if root is either A or B, then this is the target
        if root == A or root == B:
            return a, b, root

        # both child found as targets, so it is LCA
        if left_node is not None and right_node is not None:
            return a, b, root
        # left child found, return left chid
        if left_node is not None:
            return a, b, left_node
        # right child found, return right
        if right_node is not None:
            return a, b, right_node

        # nothign is found
        return a, b, None


if __name__ == "__main__":
    nodes = [4, 3, 7, None, None, 5, 6]
    nodes = [TreeNode(node) for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    a, b = nodes[5], nodes[6]
    solution = Solution()
    answer = solution.lowestCommonAncestor3(tree, a, b)
    print(answer)
