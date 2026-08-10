class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = nums + nums
        # return ans

        # ans = []
        # for i in range(2):
        #     for n in nums:
        #         ans.append(n)

        # return ans

        n = len(nums)
        ans = [0]*2*n
        # [4, 0, 0, ]

        # 0:4
        # 1:2
        # 2:0

        for i, num in enumerate(nums):
            ans[i] = num
            ans[n+i] = num

        return ans

