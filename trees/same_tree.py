# Pattern: BFS on two trees simultaneously — compare nodes level by level
# Trigger: "same tree" = compare structure + values = traverse both trees together

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                nodeP = q1.popleft()
                nodeQ = q2.popleft()

                # both None — this position matches, continue
                if nodeP is None and nodeQ is None:
                    continue

                # one None or different values — trees differ
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False

                # add children of both nodes — None children included for structure check
                q1.append(nodeP.left)
                q1.append(nodeP.right)
                q2.append(nodeQ.left)
                q2.append(nodeQ.right)

        return True