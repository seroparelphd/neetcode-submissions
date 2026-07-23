class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        cur_max = 0
        all_max = 0
        l, r = 0, 0
        while l <= r and l < len(s) and r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                cur_max += 1
                all_max = max(all_max, cur_max)
                r += 1
            # while s[r] in seen:
            else:
                seen.remove(s[l])  # seen = {"b","c"}
                cur_max -= 1
                l += 1
        return all_max


# l = 1
# r = 3
# s[r] = "a"
# seen = {"b","c","a"}
# cur_max = 3
# all_max = 3