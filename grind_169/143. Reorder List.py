# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        record = []
        node = head
        while node:
            record.append(node)
            node = node.next

        n = len(record)
        pre, nxt = 0, n - 1
        cnt = 0
        while cnt < n:
            # print("cnt, pre, nxt = ", cnt, pre, nxt)
            record[pre].next = record[nxt]
            cnt += 1
            pre = nxt
            if cnt % 2 == 1:
                nxt = n - nxt
            else:
                nxt = n - nxt - 1

        record[pre].next = None


# N: number of nodes
# TC: O(N)
# SC: O(N)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        node = head
        while node:
            nxt = node.next
            node.next = rev
            rev = node
            node = nxt
        return rev

    def mergeList(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        while l1 and l2:
            l1_nxt, l2_nxt = l1.next, l2.next

            l1.next = l2
            l1 = l1_nxt

            l2.next = l1
            l2 = l2_nxt

# N: number of nodes:
# TC: O(N)
# SC: O(1)
