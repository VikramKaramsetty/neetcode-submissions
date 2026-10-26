# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if(not root): return []
        q.append((root,1))
        res = []
        while(q):
            (node, level) = q.popleft()
            print(str(node.val) + " " + str(level))
            if(not q or q[0][1] != level): res.append(node.val)
            if(node.left):
                q.append((node.left, level+1))
            if(node.right):
                q.append((node.right, level+1))
        return res
