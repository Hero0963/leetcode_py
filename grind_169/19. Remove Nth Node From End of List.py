# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        node = head
        while node:
            size += 1
            node = node.next

        goal = size - n + 1
        if goal == 1:
            return head.next

        cnt = 1
        node = head
        while cnt < goal - 1:
            cnt += 1
            node = node.next

        node.next = node.next.next

        return head

# N: total_nodes = size
# TC: O(N)
# SC: O(1)
