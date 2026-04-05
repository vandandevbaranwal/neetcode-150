# Pattern: Tree Traversal (BFS / Level Order) — process nodes iteratively using queue
# Trigger: "invert binary tree / mirror tree" = swap children at every node → traverse all nodes

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None  # empty tree case
        
        queue = deque([root])  # BFS queue starting from root
        
        while queue:
            node = queue.popleft()
            
            # swap left and right child
            node.left, node.right = node.right, node.left
            
            # add children to queue for further processing
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root  # return inverted tree
    