# Pattern: BST Traversal
# Trigger: "Lowest Common Ancestor in BST" = use BST property to move left/right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            # both nodes are in the right subtree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right

            # both nodes are in the left subtree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left

            # split point found (or one node equals current)
            else:
                return cur