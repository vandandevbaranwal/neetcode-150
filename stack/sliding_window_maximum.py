# Pattern: Sliding Window + Monotonic Deque — maintain decreasing deque for O(n) max lookup
# Trigger: "maximum in every window" = naive O(nk) too slow = monotonic deque for O(n)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  # stores indices, values always decreasing left to right
        l = r = 0

        while r < len(nums):
            # remove smaller elements from right — they can never be the max
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left element if it's outside the window
            if l > q[0]:
                q.popleft()

            # window is fully formed — record maximum (always at front of deque)
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
'''
**Key insight to remember:**
Monotonic deque maintains elements in decreasing order — so the front is always the maximum. When a larger element enters from the right, all smaller elements behind it are useless and get popped. This is your first **monotonic deque** pattern — remember it, it appears in many hard problems. 🎯

Push it and **Sliding Window section is 100% COMPLETE!** 🔥
```
sliding_window/
├── ✅ best_time_to_buy_sell_stock.py
├── ✅ longest_substring_without_repeating.py
├── ✅ longest_repeating_character_replacement.py
├── ✅ permutation_in_string.py
├── ✅ minimum_window_substring.py
├── ✅ sliding_window_maximum.py
'''