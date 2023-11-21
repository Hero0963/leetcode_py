class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        filtered_s, filtered_t = [], []
        for c in s:
            if c != "#":
                filtered_s.append(c)
            else:
                if filtered_s:
                    filtered_s.pop()

        for c in t:
            if c != "#":
                filtered_t.append(c)
            else:
                if filtered_t:
                    filtered_t.pop()

        return filtered_s == filtered_t

# S: len(s)
# T: len(t)
# TC: O(S + T + max(S, T))
# SC: O(S + T)
