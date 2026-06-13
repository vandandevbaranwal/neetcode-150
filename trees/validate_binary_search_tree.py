# Pattern: BFS with Valid Range — pass min/max bounds down to each node
# Trigger: "validate BST" = every node must satisfy range constraint = propagate bounds

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # queue stores (node, min_bound, max_bound)
        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()

            # node value must be strictly within (left, right) bounds
            if not (left < node.val < right):
                return False

            if node.left:
                # left child must be less than current node value
                q.append((node.left, left, node.val))
            if node.right:
                # right child must be greater than current node value
                q.append((node.right, node.val, right))

        return True