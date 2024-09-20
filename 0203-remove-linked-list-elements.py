"""
203. Remove Linked List Elements
Easy
https://leetcode.com/problems/remove-linked-list-elements/

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        walker = head

        while walker and walker.next:
            if walker.next.val == val:
                walker.next = walker.next.next
            else:
                walker = walker.next

        if head and head.val == val:
            head = head.next

        return head
