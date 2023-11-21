# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        self.dummy = ListNode(0)

        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            temp, temp1, temp2 = self.dummy, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return self.dummy.next

        if not head:
            return head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummy = ListNode(0, head)
        sub_length = 1
        while sub_length < length:
            prev, curr = dummy, dummy.next
            while curr:
                head1 = curr
                for i in range(1, sub_length):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr = head2
                for i in range(1, sub_length):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break

                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None

                merged = merge(head1, head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ
            sub_length <<= 1

        return dummy.next


# N: number of nodes
# TC: O(NlogN)
# SC: O(1)
# ref = https://leetcode.cn/problems/sort-list/solutions/492301/pai-xu-lian-biao-by-leetcode-solution/


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next

        vals.sort()
        n = len(vals)

        res = ListNode()
        node = res
        for v in vals:
            node.next = ListNode(v)
            node = node.next

        return res.next

# N: number of nodes
# TC: O(NlogN + N)
# SC: O(N)
