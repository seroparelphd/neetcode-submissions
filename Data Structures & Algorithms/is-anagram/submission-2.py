class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)

        # letters = []
        # for i in range(0,len(s)):
        #     letters.append(s[i])

        # for j in range(0,len(t)):
        #     if t[j] in letters:
        #         letters.remove(t[j])
        #     else:
        #         return False

        # return True