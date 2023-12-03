# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        leng = 1
        node = head
        while node.next:
            leng += 1
            node = node.next
        last_node = node

        k = k % leng
        if k == 0:
            return head

        travel_cnt = leng - k
        curr = head
        cnt = 1
        while cnt < travel_cnt:
            cnt += 1
            curr = curr.next

        new_head = curr.next
        curr.next = None
        last_node.next = head
        return new_head

# N: number of listnodes
# TC: O(N)
# SC: O(1)
