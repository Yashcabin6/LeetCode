class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # so again I will iterate and this time I need to save index tho, and update everytime I find a new index ig?
        
        query = {}
        for i,n in enumerate(nums):
            if n in query:
                if i-query[n]<= k:
                    return True
                else:
                    query[n]=i
            else:
                query[n]=i
        return False