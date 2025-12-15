class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        query = [0]*26
        for cs,ct in zip(s,t):
            query[ord(cs)-ord('a')]+=1
            query[ord(ct)-ord('a')]-=1
        for i in query:
            if i!=0:
                return False
        return True