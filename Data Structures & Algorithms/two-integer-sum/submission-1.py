class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 3 , 4,  5, 6

        # 4 , 3, 2, 1

        map = {}
        for i, n in enumerate(nums):
            result = target - n

            if result in map:
                return [map[result], i]

            map[n] = i

        
        # 3 : 0

        
        