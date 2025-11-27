class Solution:
    def isValid(self, s: str) -> bool:
        count = [0]*3
        stk = []
        map = {')':'(','}':'{',']':'['}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stk.append(c)
            else:
                if len(stk) == 0 or stk[len(stk)-1]!= map[c]:
                    return False
                else:
                    stk.pop()
        if len(stk) == 0:
            return True
        else:
            return False
