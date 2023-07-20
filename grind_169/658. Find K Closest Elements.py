class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        x_idx = self.find_x_index(arr, x)
        # print(" x_idx = ", x_idx)
        i, j = x_idx - 1, x_idx
        while j - i + 1 < k:
            left = arr[i] if i >= 0 else -math.inf
            right = arr[j] if j < n else math.inf

            if abs(x - left) <= abs(x - right):
                i -= 1
            else:
                j += 1

        return arr[i:j + 1]

    def find_x_index(self, arr: List[int], x: int) -> int:
        # return bisect.bisect_left(arr, x)
        n = len(arr)
        head, tail = 0, n - 1
        while head <= tail:
            mid = head + (tail - head) // 2
            cur_val = arr[mid]
            # print(cur_val, head, tail)
            if cur_val > x:
                tail = mid - 1
            elif cur_val < x:
                head = mid + 1
            else:
                return mid

        return head


# by @lee215

# TC: O(log(N - K) + K)
# SC: O(K)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = left + (right - left) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left: left + k]


# TC: O(N-K + K)
# SC: O(K)


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        i, j = 0, n - 1
        while j - i + 1 != k:
            # print("i, j = ", i, j)
            left_val = arr[i] if 0 <= i < n else -math.inf
            right_val = arr[j] if 0 <= j < n and i <= j else math.inf

            if abs(x - left_val) <= abs(right_val - x):
                j -= 1
            else:
                i += 1

        return arr[i:j + 1]
