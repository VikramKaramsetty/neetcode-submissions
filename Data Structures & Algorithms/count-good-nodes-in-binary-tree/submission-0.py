# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, num):
            nonlocal count
            if(not node): return
            if(node.val >= num): count+=1

            dfs(node.left, max(num, node.val))
            dfs(node.right, max(num, node.val))

            
        dfs(root, root.val)
        return count