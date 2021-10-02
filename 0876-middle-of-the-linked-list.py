"""
876. Middle of the Linked List
Easy
https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""
from list_node import ListNode
from typing import Optional


"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(1)
        """
        if not head:
            return None

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == "__main__":
    head = [1, 2, 3, 4]
    head = ListNode.list_to_head(head)
    output = Solution().middleNode(head)
    output_str = ListNode.print(output)
    expected = [3, 4]
    expected = ListNode.list_to_head(expected)
    expected_str = ListNode.print(expected)
    print(f"\noutput\t\t{output_str}")
    print(f"expected\t{expected_str}")
    print(output_str == expected_str)

    head = [1, 2, 3, 4, 5]
    head = ListNode.list_to_head(head)
    output = Solution().middleNode(head)
    output_str = ListNode.print(output)
    expected = [3, 4, 5]
    expected = ListNode.list_to_head(expected)
    expected_str = ListNode.print(expected)
    print(f"\noutput\t\t{output_str}")
    print(f"expected\t{expected_str}")
    print(output_str == expected_str)

    head = [1, 2, 3, 4, 5, 6]
    head = ListNode.list_to_head(head)
    output = Solution().middleNode(head)
    output_str = ListNode.print(output)
    expected = [4, 5, 6]
    expected = ListNode.list_to_head(expected)
    expected_str = ListNode.print(expected)
    print(f"\noutput\t\t{output_str}")
    print(f"expected\t{expected_str}")
    print(output_str == expected_str)
