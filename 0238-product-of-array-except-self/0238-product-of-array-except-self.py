class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # make right and left product array and easy
        n = len(nums)
        right_query = [1]*n
        left_query = [1]*n
        left_query[0]=nums[0]
        right_query[n-1]=nums[n-1]
        for i in range(1,n):
            left_query[i]*=left_query[i-1]*nums[i]
            right_query[-i-1]*=right_query[-i]*nums[-i-1]
        ret = [1]*n
        ret[0] = right_query[1]
        ret[-1] = left_query[n-2]
        for i in range(1,n-1):
            ret[i]=left_query[i-1]*right_query[i+1]
        return ret