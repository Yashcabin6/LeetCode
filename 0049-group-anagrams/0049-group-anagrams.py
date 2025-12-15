class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ok so objective is to make array of groups of anagrams how will I do this?
        # ok First brute force btw arr has zip & enumerate
        # ok Edge cases string can be empty but atleast 1 string will exist how am I doing this optimally
        # ok so what I am thinking is we can make code for string and use it as key for my map????
        # ok so what's most optimal way to make key for my map????
        if len(strs)==1:
            return [strs]
        query_map = {}
        for s in strs:
            query = [0]*26
            for c in s:
                query[ord(c)-ord('a')]+=1
            key = ""
            for i in query:
                key += str(i)+' '
            if key in query_map:
                query_map[key].append(s)
            else:
                query_map[key]= [s]
        ret = []
        for key in query_map:
            ret.append(query_map[key])
        return ret