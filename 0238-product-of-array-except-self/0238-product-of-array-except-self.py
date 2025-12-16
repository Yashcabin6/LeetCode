class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # make right and left product array and easy
        n = len(nums)
        left_query = 1
        right_query = 1
        ret = [1]*n
        for i in range(n):
            ret[i]*=left_query
            ret[n-i-1]*=right_query
            left_query*=nums[i]
            right_query*= nums[n-1-i]
        return ret