# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# N: number of nodes
# TC: O(N)
# SC: O(1)

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd, even = head, head.next

        if not even:
            return odd

        cur = even.next

        ohead, ehead = odd, even
        cnt = 1
        while cur:
            if cnt % 2 == 0:
                even.next = cur
                even = even.next
            else:
                odd.next = cur
                odd = odd.next

            cur = cur.next
            cnt += 1

        even.next = None
        odd.next = ehead

        return ohead


# ref= https://leetcode.com/problems/odd-even-linked-list/solutions/133345/with-detailed-explanation-python/

class Solution:
    """
    N: length of ListNode
    time complexity: O(N)
    space complexity: O(1)
    """

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        odd = head
        even = head.next
        even_start = even

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = even_start

        return head
