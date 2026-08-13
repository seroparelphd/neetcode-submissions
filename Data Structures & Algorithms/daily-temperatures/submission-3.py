class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for day, temperature in enumerate(temperatures):
            # print(day, temperature)
            while stack and temperature > stack[-1][1]:
                prev_day, prev_temp = stack.pop()
                result[prev_day] = day - prev_day
            stack.append([day, temperature])
        #     print(stack)
        # print(stack)
        return result
