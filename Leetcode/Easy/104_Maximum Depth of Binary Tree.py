class Solution:
    def maxDepth(self, root):
        max_depth = 0 
        if root is None:
            return max_depth
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        max_depth = max(left,right) + 1
        return max_depth