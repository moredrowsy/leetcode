"""
83. Remove Duplicates from Sorted List
Easy
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""
from typing import Optional
from list_node import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(1)
        """
        if head:
            p, q = head, head.next

            while p and q:
                if p.val == q.val:
                    p.next = q.next
                else:
                    p = p.next

                q = q.next

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
