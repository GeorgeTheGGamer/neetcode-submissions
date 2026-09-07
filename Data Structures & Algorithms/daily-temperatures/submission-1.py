class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Before there is a warmer temperate , monontomically decreasing stack
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = i - stackIndex     # Concerned about the past one
            stack.append((temp,i))
        return result
            



        


