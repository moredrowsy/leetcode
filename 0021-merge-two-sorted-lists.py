"""
21. Merge Two Sorted Lists
Easy
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
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

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy

        while list1 and list2:
            if list1.val < list2.val:
                node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                list2 = list2.next

            node = node.next

        while list1:
            node.next = ListNode(list1.val)
            node = node.next
            list1 = list1.next

        while list2:
            node.next = ListNode(list2.val)
            node = node.next
            list2 = list2.next

        return dummy.next


if __name__ == "__main__":
    list1, list2 = [1, 2, 4], [1, 3, 4]
    l1 = ListNode.list_to_head(list1)
    l2 = ListNode.list_to_head(list2)
    output = Solution().mergeTwoLists(l1, l2)
    output = ListNode.head_to_array(output)
    expected = [1, 1, 2, 3, 4, 4]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    list1, list2 = [], [0]
    l1 = ListNode.list_to_head(list1)
    l2 = ListNode.list_to_head(list2)
    output = Solution().mergeTwoLists(l1, l2)
    output = ListNode.head_to_array(output)
    expected = [0]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    list1, list2 = [], []
    l1 = ListNode.list_to_head(list1)
    l2 = ListNode.list_to_head(list2)
    output = Solution().mergeTwoLists(l1, l2)
    output = ListNode.head_to_array(output)
    expected = []
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
