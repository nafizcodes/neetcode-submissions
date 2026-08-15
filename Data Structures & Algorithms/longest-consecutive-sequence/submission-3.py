# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         store = set(nums)
#         res = 0 
#         for n in nums:
#             streak = 0
#             cur = n
#             while cur in store:
#                 streak += 1
#                 cur += 1
                
#             res = max(res, streak)
#         return res
           

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 0

        for num in numSet:
            if (num-1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1

                longest = max(length, longest)

        return longest




