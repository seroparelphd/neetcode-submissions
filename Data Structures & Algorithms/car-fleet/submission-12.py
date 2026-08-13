class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        cars.sort(reverse=True)

        stack = []
        for car in cars:
            distance = target - car[0]
            time = distance / car[1]
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)