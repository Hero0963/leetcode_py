# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        p0 = dummy = ListNode(next=head)
        pre = None
        cur = head
        while n >= k:
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            nxt = p0.next
            nxt.next = cur
            p0.next = pre
            p0 = nxt

            n -= k
        return dummy.next

# N: number of nodes
# TC: O(N)
# SC: O(1)
