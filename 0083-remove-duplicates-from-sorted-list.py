"""
83. Remove Duplicates from Sorted List
Easy
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""
from typing import Optional
from list_node import ListNode


class Solution:
    """
    Time Complexity
    ---------------
    O(n)

    Space Complexity
    ----------------
    O(n)
    """

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev = head
        node = prev.next
        uniques = set([head.val])

        while node:
            if node.val in uniques:
                prev.next = node.next
                node = node.next
            else:
                uniques.add(node.val)
                prev = node
                node = node.next

        return head


if __name__ == "__main__":
    head = []
    head = ListNode.list_to_head(head)
    output = Solution().deleteDuplicates(head)
    output = ListNode.head_to_array(output)
    expected = []
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    head = [1, 1, 2]
    head = ListNode.list_to_head(head)
    output = Solution().deleteDuplicates(head)
    output = ListNode.head_to_array(output)
    expected = [1, 2]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
