# ref = https://fuxuemingzhu.cn/leetcode/146.html#%E5%AD%97%E5%85%B8-%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8
# modified by chatgpt
import collections


# Least recently used (LRU) means Discards the least recently used items first
# The functions get and put must each run in O(1) average time complexity.
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.defaultdict(int)
        self.capacity = capacity
        self.size = 0

        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove_from_list(node)
            self._insert_into_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove_from_list(node)
            self._insert_into_head(node)
            node.val = value
        else:
            if self.size >= self.capacity:
                tail_node = self.tail.prev
                del self.cache[tail_node.key]
                self._remove_from_list(tail_node)
                self.size -= 1
            node = ListNode(key, value)
            self.cache[key] = node
            self._insert_into_head(node)
            self.size += 1

    def _remove_from_list(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = None
        node.next = None

    def _insert_into_head(self, node):
        head_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_node
        head_node.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# by ordered dict
import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.dict = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1

        self.dict.move_to_end(key)

        return self.dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.move_to_end(key)
            self.dict[key] = value
        else:
            if len(self.dict) == self.capacity:
                self.dict.popitem(last=False)

            self.dict[key] = value
