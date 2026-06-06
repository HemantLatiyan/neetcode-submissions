class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        maxheap = [(-v, k) for k, v in freq.items()]
        heapq.heapify(maxheap)
        res = [ k for _, k in heapq.nsmallest(k, maxheap)]
        return res