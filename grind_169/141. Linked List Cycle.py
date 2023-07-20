# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    N = length of ListNode
    time complexity: O(N)
    space complexity: O(1)

    note that while-loop condition can be modified to a concise version, but
    this is more clear to me.

    Constraints:

    The number of the nodes in the list is in the range [0, 104].
    -10^5 <= Node.val <= 10^5
    pos is -1 or a valid index in the linked-list.
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast, slow = head, head

        while fast.next and slow:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

            if not fast or not slow:
                return False

        return False
