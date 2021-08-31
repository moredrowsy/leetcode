"""
23. Merge k Sorted Lists
Hard
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
from list_node import ListNode
from typing import List, Optional


"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.pq(lists)

    def pq(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Time Complexity
        ---------------
        O(n log n)

        Space Complexity
        ----------------
        O(n)
        """
        import heapq
        setattr(ListNode, "__lt__", lambda self, other: self.val < other.val)

        list_node = dummy = ListNode()

        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, node)

        while heap:
            l_node = heapq.heappop(heap)
            list_node.next = l_node
            list_node = list_node.next

            if l_node.next:
                heapq.heappush(heap,  l_node.next)

        return dummy.next


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists = [ListNode.get_head_from_list(l) if l else None for l in lists]
    output = Solution().mergeKLists(lists)
    output_str = ListNode.print(output)
    expected = [1, 1, 2, 3, 4, 4, 5, 6]
    expected = ListNode.get_head_from_list(expected)
    expected_str = ListNode.print(expected)
    print(f"\noutput\t\t{output_str}")
    print(f"expected\t{expected_str}")
    print(output_str == expected_str)

    lists = [[2, 6], [5], [7]]
    lists = [ListNode.get_head_from_list(l) if l else None for l in lists]
    output = Solution().mergeKLists(lists)
    output_str = ListNode.print(output)
    expected = [2, 5, 6, 7]
    expected = ListNode.get_head_from_list(expected)
    expected_str = ListNode.print(expected)
    print(f"\noutput\t\t{output_str}")
    print(f"expected\t{expected_str}")
    print(output_str == expected_str)

    lists = [[2, 4], [], [-1]]
    lists = [ListNode.get_head_from_list(l) if l else None for l in lists]
    output = Solution().mergeKLists(lists)
    output_str = ListNode.print(output)
    expected = [-1, 2, 4]
    expected = ListNode.get_head_from_list(expected)
    expected_str = ListNode.print(expected)
    print(f"\noutput\t\t{output_str}")
    print(f"expected\t{expected_str}")
    print(output_str == expected_str)

    lists = []
    lists = [ListNode.get_head_from_list(l) if l else None for l in lists]
    output = Solution().mergeKLists(lists)
    output_str = ListNode.print(output)
    expected = []
    expected = ListNode.get_head_from_list(expected)
    expected_str = ListNode.print(expected)
    print(f"\noutput\t\t{output_str}")
    print(f"expected\t{expected_str}")
    print(output_str == expected_str)

    lists = [[]]
    lists = [ListNode.get_head_from_list(l) if l else None for l in lists]
    output = Solution().mergeKLists(lists)
    output_str = ListNode.print(output)
    expected = []
    expected = ListNode.get_head_from_list(expected)
    expected_str = ListNode.print(expected)
    print(f"\noutput\t\t{output_str}")
    print(f"expected\t{expected_str}")
    print(output_str == expected_str)
