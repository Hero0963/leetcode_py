# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# N: number of nodes
# TC: O(N)
# SC: O(N)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next

        i, j = 0, len(vals) - 1
        while i < j:
            if vals[i] != vals[j]:
                return False

            i += 1
            j -= 1

        return True


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# ref = https://leetcode.com/problems/palindrome-linked-list/solutions/612914/python-go-o-1-aux-space-by-two-pointers-w-hint/

# N: number of nodes
# TC: O(N)
# SC: O(1)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        tail = self.reverse_linked_list(slow)

        # we can also cnt half_length
        while tail:
            if tail.val != head.val:
                return False

            head, tail = head.next, tail.next

        return True

    def reverse_linked_list(self, node: ListNode) -> ListNode:
        prev, cur = None, node
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev
