# Pattern: Monotonic Stack — maintain decreasing stack, pop when warmer temp found
# Trigger: "next greater element" = look ahead for something larger = monotonic stack

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)  # default 0 = no warmer day found
        stack = []  # stores [temperature, index] in decreasing order

        for i, t in enumerate(temperatures):
            # pop all days that are colder than today — today is their answer
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)  # days waited = current index - stored index
            stack.append([t, i])

        return res