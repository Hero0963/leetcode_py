# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# N: number of nodes
# TC: O(N)
# SC: O(1)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        total_step = 0
        cur_node = head
        while cur_node:
            cur_node = cur_node.next
            total_step += 1

        half_step = total_step // 2
        step = 0
        cur_node = head
        while step < half_step:
            # print(cur_node.val)
            cur_node = cur_node.next
            step += 1

        return cur_node


# N: number of nodes
# TC: O(N)
# SC: (N)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
