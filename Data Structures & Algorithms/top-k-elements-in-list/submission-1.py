class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        pairs = [ (-v, k) for k,v in freq.items()]
        heapq.heapify(pairs)
        res = []
        while k > 0:
            _, key = heapq.heappop(pairs)
            res.append(key)
            k -= 1
        return res
        
