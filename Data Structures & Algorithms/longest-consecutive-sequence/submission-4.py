class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set(nums)
        # print(numset)
        for num in numset:
            streak, curr = 0, num
            while curr in numset:
                streak += 1
                curr += 1
            res = max(streak, res)
        return res


