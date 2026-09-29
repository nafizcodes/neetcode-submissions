# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         # res = 0 
#         # area = 0

#         # for i in range(len(heights)):
#         #     for j in range(i+1, len(heights)):
#         #         area = max(area, min(heights[i],heights[j])*(j-i))
#         # return area

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        area = 0 

        while l < r:
            area = max(area, min(heights[l], heights[r]) * (r-l))

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return area

        