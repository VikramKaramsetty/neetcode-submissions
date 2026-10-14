# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        best = 0
        def dfs(node):
            nonlocal best
            if(not node): return 0

            right = dfs(node.right)
            left = dfs(node.left)
            
            best = max(best, right + left)
            return 1 + max(right, left)

        dfs(root)
        return best