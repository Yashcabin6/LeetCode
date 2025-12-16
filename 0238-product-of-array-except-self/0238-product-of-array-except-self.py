class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # make right and left product array and easy
        n = len(nums)
        query = 1
        ret = [1]*n
        for i in range(n):
            ret[i]*=query
            query*=nums[i]
        query = 1
        for i in range(n):
            ret[n-i-1]*=query
            query*= nums[n-1-i]
        return ret