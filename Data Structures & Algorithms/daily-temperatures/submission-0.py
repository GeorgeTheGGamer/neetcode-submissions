class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #O(n) solution
        # Each entry in the result is the number of days after the ith day that there is a greater temperature
        # Monotonic Decreasing order

        stack = []
        result = [0] * len(temperatures)

        # Push the value and it's position to the stack then take the difference

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = i - stackIndex
            stack.append((temp, i))        

        return result


        


