# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        if not head.next:
            return head

        p = ListNode(-1)
        node = p
        cur = head
        stack = []

        while cur:
            stack.append(cur)
            cur = cur.next

            if len(stack) == 2:
                node.next = stack.pop()
                node.next.next = stack.pop()
                node = node.next.next

        if stack:
            node.next = stack.pop()
            node = node.next

        node.next = None

        return p.next

# N: number of nodes
# TC: O(N)
# SC: O(1)
