class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1 

        while l <= r:
            mid = (l+r) //2
        # 4 5 6 7 0 1 2 3

            if nums[mid] == target:
                return mid
            # left portion
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1 
                else:
                    l = mid + 1
            #right portion
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

                    
            
        # l = 0
        # r = len(nums)-1
        # # 4 5 6 7 0 1 2 
                 
        # while l <= r:
        #     mid = l + r // 2

        #     if nums[m] >= l:
        #         l = m + 1
        #     else:
        #         r = m

        # pivot = l

        # l, r = 0, len(nums)-1

        # while l <= r:
        #     m = (l+r) // 2
        #     if nums[m] == target:
        #         return m
        #     elif nums[m] >= pivot:





        













            


            