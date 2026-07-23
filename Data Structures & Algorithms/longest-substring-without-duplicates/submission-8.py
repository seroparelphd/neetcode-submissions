class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        cur_max = 0
        all_max = 0
        l, r = 0, 0
        # while l <= r and l < len(s) and r < len(s):
        while r < len(s):
            if s[r] in seen:
                last_seen_index_of_char = seen[s[r]]
                l = max(l, last_seen_index_of_char + 1)
            seen[s[r]] = r
            all_max = max(all_max, r - l + 1)
            r += 1
        return all_max

# l = 2
# r = 3
# s[r] = "k"
# last_seen_index_of_char = 1
# seen = {"p": 0, "w": 1, }
# cur_max = 2
# all_max = 2