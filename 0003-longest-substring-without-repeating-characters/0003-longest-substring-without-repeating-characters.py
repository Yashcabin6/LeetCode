class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        s1 = set()
        ret = 0
        for c in s:
            while c in s1 and l < r:
                s1.remove(s[l])
                l+=1
            s1.add(c)
            r+=1
            ret = max(ret,r-l)
        return ret