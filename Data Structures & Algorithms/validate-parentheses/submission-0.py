class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "}":"{","]":"["}
        for i in s:
            if i in closeToOpen:
                if stack and stack[-1] and closeToOpen[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack