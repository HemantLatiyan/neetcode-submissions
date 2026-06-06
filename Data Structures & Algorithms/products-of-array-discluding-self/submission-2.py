class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product_left = [1]*(n)
        for i in range(1,n):
            product_left[i] = product_left[i-1] * nums[i-1]
        # print(product_left)

        suffix = 1
        for i in range(n-1, -1, -1):
            product_left[i] *= suffix
            suffix *= nums[i]
            
        return product_left