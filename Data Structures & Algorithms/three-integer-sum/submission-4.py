class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [ - 1, 0, 1 ,2 , -1, -4]
        res = []
        nums.sort()   # to avoid duplicates
        # -4, -1, -1, 0 , 1, 2
        for i, a in enumerate(nums):

            if a > 0:
                break

            if i > 0 and a == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                cur = a + nums[l] + nums[r]

                if cur > 0:
                    r -= 1
                elif cur <0 :
                    l += 1

                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res            
                    # [-2,-2, 0, 0, 2, 2]

                    # only shift left, 
                    # the other pointer will be handled inside the loop
                    





            
            
            


        return res
