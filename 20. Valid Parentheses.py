class Solution:
    def isValid(self,s):
        stack = []
        bracketmatch = {')' : '(' , '}':'{' , ']' : '['}
        for v in s:
            if v in bracketmatch:
                if stack and stack[-1] == bracketmatch[v]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(v)
        return not stack
s = '()[]{}'
sol = Solution()
print(sol.isValid(s))
