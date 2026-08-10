class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     l = 0
    #     r = len(nums)-1

    #     while l <= r:
    #         mid = (l + r) // 2

    #         if nums[mid] == target:
    #             return mid
    #         elif nums[mid] < target:    
    #             l = mid + 1
    #         else:
    #             r = mid - 1

    #     return -1

    def bs(self, l, r, nums, target) -> int:
        if l > r:
            return -1

        m = l + (r-l) // 2
        if nums[m] == target:
            return m
        if nums[m] > target:
            return self.bs(l, m - 1, nums, target)
        else:
            return self.bs(m + 1, r, nums, target)

    def search(self, nums:List[int], target:int) -> int:
        return self.bs(0, len(nums)-1, nums, target)
