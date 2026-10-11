class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # (temp, index)
        stack = []
        
        # for each temp 
            # continue popping until stack top is no longer < temp

            # append temp
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = (i - stackIndex)

            stack.append((temp, i))

        return result

        