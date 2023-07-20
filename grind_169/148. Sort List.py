# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# N: number of nodes
# TC: O(NlogN + N)
# SC: O(N)

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next

        vals.sort()
        n = len(vals)

        res = ListNode()
        node = res
        for v in vals:
            node.next = ListNode(v)
            node = node.next

        return res.next
