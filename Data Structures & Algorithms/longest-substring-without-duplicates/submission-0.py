class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        cur_max = 0
        all_max = 0
        l, r = 0, 0
        # for i in range(len(s)):
        while l <= r and l < len(s) and r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                cur_max += 1
                all_max = max(all_max, cur_max)
                r += 1         
            else:
                l += 1
                r = l
                cur_max = 0
                seen = set()
        return all_max


# l = 1
# r = 1
# s[r] = "c"
# seen = {"a","b","c"}
# cur_max = 3