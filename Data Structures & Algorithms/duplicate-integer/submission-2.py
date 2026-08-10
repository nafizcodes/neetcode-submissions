class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # n = 1 1 2 3 3

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        sorted = nums.sort() # O(n)> nlogn
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False





            