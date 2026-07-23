class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        cur_max = 0
        all_max = 0
        l, r = 0, 0
        while l <= r and l < len(s) and r < len(s):
            if s[r] not in seen:
                seen[s[r]] = r
                cur_max = r - l + 1
                all_max = max(all_max, cur_max)
                r += 1
            else:
                last_seen_index_of_char = seen[s[r]]
                l = max(l, last_seen_index_of_char + 1)
                del seen[s[r]]
        return all_max

# l = 0
# r = 2
# s[r] = "w"
# last_seen_index_of_char = 1
# seen = {"p": 0, "w": 2}
# cur_max = 1
# all_max = 2