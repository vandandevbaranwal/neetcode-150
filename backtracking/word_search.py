# Pattern: Backtracking + DFS on Grid
# Trigger: "search a word in a grid" = explore all paths while marking visited cells

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            # entire word matched
            if i == len(word):
                return True

            # out of bounds, wrong character, or already visited
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] == '#' or
                board[r][c] != word[i]
            ):
                return False

            # mark current cell as visited
            board[r][c] = '#'

            # explore all four directions
            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            # restore original character (backtrack)
            board[r][c] = word[i]

            return found

        # try every cell as a starting point
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False
    