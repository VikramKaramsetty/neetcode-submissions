# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q) -> bool:
            if not p and not q: return True
            if(not (p and q)): return False
            if(p.val != q.val): return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        ans = False
        def dfs(node, subRoot):
            nonlocal ans 
            if not node: return

            if(isSameTree(node, subRoot)):
                ans = True
                return
            dfs(node.left, subRoot)
            dfs(node.right, subRoot)

        dfs(root, subRoot)
        return ans 