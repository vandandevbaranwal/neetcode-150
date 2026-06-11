# Pattern: BFS with State Tracking
# Trigger: "good node" = compare current node with maximum value seen on path from root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()

        # store: (node, max_value_seen_so_far_on_path)
        q.append((root, -float('inf')))

        while q:
            node, maxval = q.popleft()

            # current node is good if no larger value exists on its path
            if node.val >= maxval:
                res += 1

            # pass updated maximum to children
            if node.left:
                q.append((node.left, max(maxval, node.val)))

            if node.right:
                q.append((node.right, max(maxval, node.val)))

        return res