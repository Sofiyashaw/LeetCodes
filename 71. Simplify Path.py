class Solution:
    def simplifyPath(self,path):
        stack = []
        cur = ""

        for c in path + "/":
            if c == "/":
               if cur == "..":
                  stack and stack.pop()
               elif cur != "." and cur != "":
                  stack.append(cur)
               cur = ""
 
            else:
               cur += c
        return "/" + "/".join(stack)
path = "/home/Document/../you"
sol = Solution()
print(sol.simplifyPath(path))
