# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node, level):
            if(not node): return

            if(level == len(ans)): ans.append([node.val])
            else: ans[level].append(node.val)

            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 0)

        ans2 = []
        for i in range(len(ans)):
            ans2.append(ans[i][-1])
        return ans2