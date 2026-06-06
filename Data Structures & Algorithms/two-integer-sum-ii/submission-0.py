class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        twosum = numbers[l] + numbers[r]
        while twosum != target:
            if twosum > target:
                r -= 1
            else:
                l += 1
            twosum = numbers[l] + numbers[r]
        return [l+1, r+1]