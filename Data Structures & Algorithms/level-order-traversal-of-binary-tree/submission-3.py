# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Return Level order
        result = []
        queue = collections.deque()
        if not root:
            return []
        queue.append(root)

        while queue:
            level = []
            queueLength = len(queue)
            for i in range(queueLength):
                currentNode = queue.popleft()
                if currentNode:
                    level.append(currentNode.val)
                    queue.append(currentNode.left)
                    queue.append(currentNode.right)

            if level:
                result.append(level)
        
        return result




        
        



        




        