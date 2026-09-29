class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # l = 0 
        # r = len(nums)-1


        # while l < r:
        #     curSum = numbers[l] + numbers[r]

        #     if curSum < target:
        #         r =- 1
        #     elif curSum > target:
        #         l += 1

        #     else:
        #         return [l+1, r+1]


        
        map = {}
        for i, n in enumerate(numbers):
            result = target - n

            if result in map:
                return [map[result]+1, i+1]

            map[n] = i
