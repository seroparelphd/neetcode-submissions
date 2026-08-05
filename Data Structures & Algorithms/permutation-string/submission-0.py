from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        print(f"target = {target}")
        window = Counter()
        l = 0
        for r in range(len(s2)):
            window[s2[r]] += 1  # Add new char
            if r - l + 1 > len(s1):
                window[s2[l]] -= 1  # Remove left char
                l += 1  # Next char
            if window == target:
                return True
        return False


# s1 = "abc", s2 = "lecabee"
#                   l
#                   r
# r - l + 1 = 1