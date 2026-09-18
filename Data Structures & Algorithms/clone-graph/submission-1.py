"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        def dfs(node):
            if not node:
                return None
            # If this node has already been copied then return it
            if node in old_to_new:
                return old_to_new[node]
            
            # Else make a copy
            copy = Node(node.val)
            old_to_new[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            # Then we return all the way back up to return clone
            return copy
        
        return dfs(node)
            
        