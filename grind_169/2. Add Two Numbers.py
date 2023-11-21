# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        record_v1 = self.get_node_vals(l1)
        record_v2 = self.get_node_vals(l2)
        v1 = self.convert_reversed_list_vals_to_int(record_v1)
        v2 = self.convert_reversed_list_vals_to_int(record_v2)
        v = v1 + v2
        if not v:
            return ListNode(0)

        res = ListNode()
        node = res
        while v:
            v, r = divmod(v, 10)
            node.next = ListNode(val=r)
            node = node.next

        return res.next

    def get_node_vals(seld, node):
        record = []
        while node:
            record.append(node.val)
            node = node.next

        return record

    def convert_reversed_list_vals_to_int(self, ls):
        x = 0
        n = len(ls)
        for i in range(n - 1, -1, -1):
            x *= 10
            x += ls[i]

        return x


# N: number of nodes in l1
# M: number of nodes in l2
# TC: O(N + M)
# SC: O(N+ M)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            v = v1 + v2 + carry
            carry, r = divmod(v, 10)
            res.next = ListNode(r)

            res = res.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

# N: number of nodes in l1
# M: number of nodes in l2
# TC: O(N + M)
# SC: O(1)
