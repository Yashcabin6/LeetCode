class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # As I iterate I will check if element exists behind me if not add elemet and move on
        query = set()
        for i in nums:
            if i in query:
                return True
            query.add(i)
        return False