# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        node = head
        while node:
            nxt = node.next
            node.next = rev
            rev = node
            node = nxt

        return rev


# N: number of nodes
# TC: O(N)
# SC: O(1)