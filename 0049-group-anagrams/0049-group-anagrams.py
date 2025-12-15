from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ok so objective is to make array of groups of anagrams how will I do this?
        # ok First brute force btw arr has zip & enumerate
        # ok Edge cases string can be empty but atleast 1 string will exist how am I doing this optimally
        # ok so what I am thinking is we can make code for string and use it as key for my map????
        # ok so what's most optimal way to make key for my map????
        # one important syntax is included ok what is it??? query_map = defaultdict(list), this will make map to list by default
        if len(strs)==1:
            return [strs]
        query_map = defaultdict(list)
        for s in strs:
            query = [0]*26
            for c in s:
                query[ord(c)-ord('a')]+=1
            key = tuple(query)
            query_map[key].append(s)
        ret = []
        for key in query_map:
            ret.append(query_map[key])
        return ret