# Pattern: Binary Search twice — first find the row, then find the target in that row
# Trigger: "sorted matrix + find target" = treat as two separate binary searches

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        # Step 1 — binary search to find the correct row
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1      # target is below this row
            elif target < matrix[row][0]:
                bot = row - 1      # target is above this row
            else:
                break              # target must be in this row

        if not (top <= bot):
            return False           # target not in any row

        # Step 2 — binary search within the identified row
        row = (top + bot) // 2
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
    