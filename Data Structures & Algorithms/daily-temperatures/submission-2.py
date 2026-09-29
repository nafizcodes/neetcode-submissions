class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        #  73, 71, 75, 71, 679, 72, 76
        # stack = (73,0)
  # res =  1 , 1 , 
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd

            stack.append((t,i))
        return res