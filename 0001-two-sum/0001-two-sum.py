class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        query = {}  # Hash map for storing remainder and key pair
        for i in range(len(nums)):
            if nums[i] in query:
                return [query[nums[i]],i]   # if remainder is same as current scan we can return 
            else:
                query[target-nums[i]]=i;    # storing remainder with key
        