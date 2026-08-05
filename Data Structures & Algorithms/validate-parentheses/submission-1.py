class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            "(": ")",
            "{": "}",
            "[": "]"
            }
        stack = []
        for char in s:
            if char in valid:
                stack.append(char)
            else:
                if not stack:
                    return False
                open_char = stack.pop()
                if valid[open_char] != char:
                    return False
        return len(stack) == 0

            