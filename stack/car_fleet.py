# Pattern: Monotonic Stack — sort by position, use stack to track distinct fleets
# Trigger: "cars merging into fleets" = compare arrival times = sort + stack

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)  # sort by position, closest to target first

        stack = []
        for p, s in pair:
            # calculate time for this car to reach target
            stack.append((target - p) / s)
            # if current car arrives <= car ahead, it joins that fleet
            # pop current car — it merges and won't form a new fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        # each element remaining in stack = one distinct fleet
        return len(stack)