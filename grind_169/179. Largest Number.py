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

# N: len(nums)
# M: largest digits in nums
# TC: O(NlogN*M)
# SC: O(NlogN*M)
