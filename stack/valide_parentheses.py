# Pattern: Stack — track opening brackets and match them with closing ones
# Trigger: "valid parentheses / balanced brackets" = LIFO structure needed → stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # holds opening brackets
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }  # mapping for matching pairs
        
        for c in s:
            # if it's a closing bracket → check for valid match
            if c in closeToOpen:
                # stack not empty AND top matches corresponding opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()  # valid pair → remove opening
                else:
                    return False  # mismatch or no opening available
            
            else:
                stack.append(c)  # push opening bracket
        
        # valid only if no unmatched opening brackets remain
        return True if not stack else False