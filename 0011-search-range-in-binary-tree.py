"""
11. Search Range in Binary Search Tree
Medium
https://www.lintcode.com/problem/11/

Given a binary search tree and a range [k1, k2], return node values within a given range in ascending order.
"""

from tree_node import TreeNode


class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        output = []
        self.dfs(root, k1, k2, output)
        return output

    def dfs(self, node, k1, k2, output):
        if node:
            if node.val > k1:
                self.dfs(node.left, k1, k2, output)

            if k1 <= node.val <= k2:
                output.append(node.val)

            if node.val < k2:
                self.dfs(node.right, k1, k2, output)


if __name__ == "__main__":
    nodes = [20, 8, 22, 4, 12]
    k1 = 6
    k2 = 10
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().searchRange(tree, k1, k2)
    expected = [8]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nodes = [31, 11, 51, 8,  None, 41, 61]
    k1 = 9
    k2 = 52
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().searchRange(tree, k1, k2)
    expected = [11, 31, 41, 51]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nodes = [20, 1, 40,  None, None, 35]
    k1 = 17
    k2 = 37
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().searchRange(tree, k1, k2)
    expected = [20, 35]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
