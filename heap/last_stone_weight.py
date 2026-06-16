# Pattern: Bucket Sort / Frequency Counting
# Trigger: Small bounded values (stone weights ≤ 1000) = count frequencies instead of using a heap

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxStone = max(stones)

        # bucket[i] = frequency of stone weight i
        bucket = [0] * (maxStone + 1)

        for stone in stones:
            bucket[stone] += 1

        first = second = maxStone

        while first > 0:

            # even count cancels itself out
            if bucket[first] % 2 == 0:
                first -= 1
                continue

            # find next largest stone
            j = min(first - 1, second)

            while j > 0 and bucket[j] == 0:
                j -= 1

            # no second stone exists
            if j == 0:
                return first

            second = j

            # smash the two stones
            bucket[first] -= 1
            bucket[second] -= 1

            # add remaining stone
            bucket[first - second] += 1

            # continue from largest possible candidate
            first = max(first - second, second)

        return first