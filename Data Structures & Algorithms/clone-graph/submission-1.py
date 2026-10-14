"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        root = Node(1, [])
        if not node: return None
        nodemap = {}
        def dfs(node, copy):
            copy.val = node.val
            copy.neighbors = [] 
  
            nodemap[node] = copy #visited
            for i in node.neighbors:
                if(i not in nodemap):
                    nextNode = Node()
                    copy.neighbors.append(nextNode)
                    dfs(i, nextNode)
                else:
                    copy.neighbors.append(nodemap.get(i))

        dfs(node, root)
        return root