"""
2. Add Two Numbers
Medium
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional
from list_node import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = int(self.dfs(l1))
        num2 = int(self.dfs(l2))
        num = str(num1 + num2)

        dummy = ListNode()
        node = dummy

        while num:
            n = len(num)
            val = num[n-1]
            num = num[:n-1]

            node.next = ListNode(val)
            node = node.next

        return dummy.next

    def dfs(self, root: Optional[ListNode]):
        if root.next is None:
            return root.val

        return str(self.dfs(root.next)) + str(root.val)


if __name__ == "__main__":
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    l1 = ListNode.list_to_head(l1)
    l2 = ListNode.list_to_head(l2)
    output = Solution().addTwoNumbers(l1, l2)
    output = ListNode.head_to_array(output)
    expected = [7, 0, 8]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    l1 = [0]
    l2 = [0]
    l1 = ListNode.list_to_head(l1)
    l2 = ListNode.list_to_head(l2)
    output = Solution().addTwoNumbers(l1, l2)
    output = ListNode.head_to_array(output)
    expected = [0]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    l1 = ListNode.list_to_head(l1)
    l2 = ListNode.list_to_head(l2)
    output = Solution().addTwoNumbers(l1, l2)
    output = ListNode.head_to_array(output)
    expected = [8, 9, 9, 9, 0, 0, 0, 1]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    l1 = [2, 4, 9]
    l2 = [5, 6, 4, 9]
    l1 = ListNode.list_to_head(l1)
    l2 = ListNode.list_to_head(l2)
    output = Solution().addTwoNumbers(l1, l2)
    output = ListNode.head_to_array(output)
    expected = [7, 0, 4, 0, 1]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
