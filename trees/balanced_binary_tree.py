# Pattern: Iterative Postorder DFS — process children before parent, track heights
# Trigger: "balanced tree" = check height difference at every node = postorder traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root):
        stack = []
        node = root
        last = None
        depths = {}     # stores height of each processed node

        while stack or node:
            if node:
                # go as far left as possible
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    # both children processed — process current node
                    stack.pop()
                    left = depths.get(node.left, 0)
                    right = depths.get(node.right, 0)

                    # unbalanced if height difference > 1
                    if abs(left - right) > 1:
                        return False

                    depths[node] = 1 + max(left, right)
                    last = node    # mark as processed
                    node = None
                else:
                    # process right child next
                    node = node.right

        return True