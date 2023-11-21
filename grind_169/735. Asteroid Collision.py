class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        stack = []
        for x in asteroids:
            if x > 0:
                stack.append(x)
            elif x < 0:
                result = x
                while stack:
                    y = stack.pop()
                    result = y + x
                    if result > 0:
                        stack.append(y)
                        break
                    elif result == 0:
                        break
                    else:
                        pass

                if not stack and result < 0:
                    ans.append(x)

        ans += stack
        return ans

# N: len(asteroids)
# TC: O(N)
# SC: O(N)
