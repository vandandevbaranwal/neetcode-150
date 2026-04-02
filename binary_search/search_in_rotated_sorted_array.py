# Pattern: Binary Search twice — find pivot first, then binary search in correct half
# Trigger: "search in rotated sorted array" = find rotation point first = two binary searches

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # Step 1 — find pivot (index of minimum element = rotation point)
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1      # minimum is in right half
            else:
                r = m          # minimum is in left half (including mid)

        pivot = l              # pivot = index of smallest element

        # Step 2 — binary search in both halves around pivot
        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        # search left half (before pivot)
        result = binary_search(0, pivot - 1)
        if result != -1:
            return result

        # search right half (from pivot onwards)
        return binary_search(pivot, len(nums) - 1)