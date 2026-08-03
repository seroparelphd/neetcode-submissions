class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[r])
            longest = max(longest, r - l + 1)
        return longest

# s = "pwwkew"
#       lr
#
# l = 1, s[l] = w
# r = 2, s[r] = w
# substring = {p, w}
# longest = 1

# s = "zxyzxyz"
#         r
#
# l = 0
# r = 3
# s[l] = z
# s[r] = z
# substring = {z, x, y}
# longest = 3

