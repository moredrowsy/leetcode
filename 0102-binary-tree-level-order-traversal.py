"""
102. Binary Tree Level Order Traversal
Medium
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
from tree_node import TreeNode
from typing import List


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        output = []

        if root:
            queue = [root]

            while queue:
                level_output = []

                n = len(queue)
                for _ in range(n):
                    node = queue.pop(0)
                    level_output.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                output.append(level_output)
                level_output = []

        return output


if __name__ == "__main__":
    nodes = [3, 9, 20, None, None, 15, 7]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().levelOrder(tree)
    expected = [[3], [9, 20], [15, 7]]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
