# ref = https://leetcode.com/problems/largest-number/solutions/213599/thinking-process-in-python/

# N: len(nums)
# TC: O(NlogN)
# SC: O(N)

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp_func(x, y):
            """Sorted by value of concatenated string increasingly."""
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1

        ls = list(str(x) for x in nums)
        ls.sort(key=cmp_to_key(cmp_func), reverse=True)
        ans = "".join(ls).lstrip("0") or "0"

        return ans


# ref = leetcode sample code

# N: len(nums)
# TC: O(NlogN)
# SC: O(N)

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ls = list(str(x) for x in nums)
        ls.sort(key=lambda x: x * 10, reverse=True)
        ans = "".join(ls).lstrip("0") or "0"

        return ans
