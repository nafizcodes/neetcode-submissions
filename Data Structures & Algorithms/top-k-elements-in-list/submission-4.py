# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}

#         freq = [[] for i in range(len(nums)+1)]
        
#         for n in nums:
#             count[n] = 1 + count.get(n,0)

#         for n,c in count.items():
#             freq[c].append(n)

#         res = []
#         for i in range(len(freq)-1, 0, -1):
#             for num in freq[i]:    
#                 res.append(num)
#                 if len(res) == k:
#                     return res
        
        

        
# [[],[1],[2],[3],[],[]]
# Find top k frequent numbers:

# Count → Bucket → Backwards → K

# HashMap:
# number → frequency

# Buckets:
# frequency → numbers

# Scan:
# high frequency → low frequency

# Stop:
# len(result) == k

# Time: O(n)
# Space: O(n)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # nums = [1,1,1,2,2,3]

        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
#            map = { 1:3, 2:2, 3:1}
        heap = []
        for num in count:
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k :
                heapq.heappop(heap)

        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        # for n in heap:
        #     res.append(heapq.heappop(heap)[1])
        return res

#         1
#     1          1 
# 2      2     3

#         map = { 1:3, 2:2, 3:1}

#         1
#     2      3

#     k = 2

#     2
#   3




























        