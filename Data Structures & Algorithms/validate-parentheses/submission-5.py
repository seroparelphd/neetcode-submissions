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
                open_brackets = stack.pop()
                if valid[open_brackets] != char:
                    return False
        return len(stack) == 0

# s = "([{}])"
# stack = ["(", "[", "{"]
# open_brackets = 
            