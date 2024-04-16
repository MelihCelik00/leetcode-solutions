from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        brackets = {")": "(", "}": "{", "]": "["}

        for p in s:
            if p in brackets.values():
                stack.append(p)
            elif stack and brackets[p] == stack[-1]:
                stack.pop()
            else:
                return False

        return len(stack) == 0