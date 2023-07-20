# ref = https://leetcode.com/problems/merge-k-sorted-lists/solutions/203549/python-solution/
# N: total number of nodes
# K: number of linkedlists
# TC: O(N * logK)
# SC: O(N + K)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        heap = [(lists[i].val, i) for i in range(n) if lists[i]]
        heapq.heapify(heap)
        head = None
        while heap:
            nxt = heapq.heappop(heap)
            node, idx = ListNode(nxt[0]), nxt[1]
            if not head:
                head = node
                cur = head
            else:
                cur.next = node
                cur = cur.next

            if lists[idx].next:
                lists[idx] = lists[idx].next
                heapq.heappush(heap, (lists[idx].val, idx))

        return head
