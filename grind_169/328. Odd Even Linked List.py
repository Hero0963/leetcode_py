# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        if not head.next:
            return head

        ohead, ehead = head, head.next
        p, q = head, head.next
        cur = q.next
        cnt = 1
        while cur:
            if cnt % 2 == 0:
                q.next = cur
                q = q.next
            else:
                p.next = cur
                p = p.next

            cur = cur.next
            cnt = (cnt + 1) % 2

        q.next = None
        p.next = ehead

        return ohead

# N: number of nodes
# TC: O(N)
# SC: O(1)
