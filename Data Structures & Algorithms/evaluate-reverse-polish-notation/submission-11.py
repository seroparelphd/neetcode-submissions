class Solution:
    def is_number(self, string) -> bool:
        try:
            float(string)
            return True
        except ValueError:
            return False
    def evalRPN(self, tokens: List[str]) -> int:
        nums_stack = []
        res = 0
        for t in tokens:
            # print(f"t = {t}")
            # print(True if t.isalnum() else False)
            if self.is_number(t):
                nums_stack.append(int(t))
                # print(f" appending {t} to stack; nums_stack = {nums_stack}")
            else:
                val1 = nums_stack.pop()
                val2 = nums_stack.pop()
                # print(f" nums_stack.pop(), nums_stack.pop() = {nums_stack.pop(), nums_stack.pop()}")
                if t == "+":
                    # print(f"nums_stack.pop() + nums_stack.pop() = {nums_stack.pop()} + {nums_stack.pop()}")
                    # res = nums_stack.pop() + nums_stack.pop()
                    res = val1 + val2
                elif t == "-":
                    # res = nums_stack.pop() - nums_stack.pop()
                    res = val2 - val1
                elif t == "*":
                    # res = nums_stack.pop() * nums_stack.pop()
                    res = val1 * val2
                else:
                    # res = int(nums_stack.pop() / nums_stack.pop())
                    res = int(val2/val1)
                nums_stack.append(res)  
            # print(f"nums_stack = {nums_stack}")
        return nums_stack[-1]