class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []
        n = len(arr)
        x_idx = self.find_x_index(arr, x)
        i, j = x_idx - 1, x_idx
        cnt = 0
        last_i, last_j = j, i
        while cnt < k:
            left = arr[i] if i >= 0 else -math.inf
            right = arr[j] if j < n else math.inf

            if abs(x - left) <= abs(x - right):
                cnt += 1
                last_i = i
                i -= 1
            else:
                cnt += 1
                last_j = j
                j += 1

        res = arr[last_i:last_j + 1]
        return res

    def find_x_index(self, arr: List[int], x: int) -> int:
        return bisect.bisect_left(arr, x)

# N: len(arr)
# K : k
# TC: O(logN + K)
# SC: O(K)
