class Solution:
    def isValid(self, s: str) -> bool:
        

        stack = []
        bracketMap = {}
        bracketMap["}"] = "{"
        bracketMap["]"] = "["
        bracketMap[")"] = "("

        for b in s:
            if b in bracketMap:
                if not stack:
                    return False
                else:
                    stackVal = stack.pop()
                    if stackVal != bracketMap[b]:
                        return False

            else:
                stack.append(b)
            
        return not stack