class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s2 = s.replace(" ", "").lower()
        # print(s2)
        s2 = ""
        for char in s:
            if char.isalnum():
                # s2.add(char.lower())
                s2 += char.lower()
        print(s2)
        return s2 == s2[::-1]