"""
19. Remove Nth Node From End of List
Medium
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?
"""
from typing import Optional
from list_node import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Algorithm
        ---------
        Idea is to keep two nodes.

        1. Reference the head node as the pre_delete node
        2. head node will move by the first nth node
        3. At this point, the pre_delete node and head node is nth difference
        4. Move head node (along with the pre_delete node in sync) to the end.
        5. When the head node is at the end, the pre_delete node is already
           at the nth last node (because of the difference from #3)
        6. Rearrange the pre_delete node to the next node

        NOTE
        ----
        Implementation uses dummy node as the third node so the pre_delete
        moves by next's next.

        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(1)
        """
        dummy = ListNode(0)
        dummy.next = head
        pre_delete = dummy

        for _ in range(n):
            head = head.next

        while head:
            head = head.next
            pre_delete = pre_delete.next

        pre_delete.next = pre_delete.next.next
        return dummy.next


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = 2
    head = ListNode.list_to_head(head)
    output = Solution().removeNthFromEnd(head, n)
    output = ListNode.head_to_array(output)
    expected = [1, 2, 3, 4, 5, 6, 7, 9]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    head = [1]
    n = 1
    head = ListNode.list_to_head(head)
    output = Solution().removeNthFromEnd(head, n)
    output = ListNode.head_to_array(output)
    expected = []
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    head = [1, 2]
    n = 1
    head = ListNode.list_to_head(head)
    output = Solution().removeNthFromEnd(head, n)
    output = ListNode.head_to_array(output)
    expected = [1]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
