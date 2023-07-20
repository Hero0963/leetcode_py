# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# N: number of listnode
# TC: O(N)
# SC: O(1)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_length = 0
        cur = head
        while cur:
            total_length += 1
            cur = cur.next

        # assuming 0-indexed
        remove_idx = total_length - n
        cur_idx = 0

        # 0 <= original node.val <= 30
        prev_node = ListNode(-1)
        nxt_node = ListNode(-1)

        if remove_idx == 0:
            head = head.next
            cur_idx += 1

        cur = head
        while cur:
            if cur_idx == remove_idx - 1:
                prev_node = cur

            if cur_idx == remove_idx + 1:
                nxt_node = cur
                break

            cur = cur.next
            cur_idx += 1

        if nxt_node.val != -1:
            prev_node.next = nxt_node
        else:
            prev_node.next = None

        return head


from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    N: the length of linked-list
    time complexity: O(N)
    space complexity: O(1)
    """

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        count = 1
        cur = head

        while cur:
            sz += 1
            cur = cur.next

        goal = (sz - n + 1)

        if n == sz:
            return head.next

        p = head
        while count < goal - 1:
            count += 1
            p = p.next

        p.next = p.next.next

        return head