class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            s1 = heapq.heappop(maxHeap)
            s2 = heapq.heappop(maxHeap)

            if s2 > s1:
                res = s1 - s2  # -8 - (-7) = -1
                heapq.heappush(maxHeap, res)
        maxHeap.append(0)
        return abs(maxHeap[0])



# maxheap
# pop 2
# calculate
# push to the heap

# keep doing until heap