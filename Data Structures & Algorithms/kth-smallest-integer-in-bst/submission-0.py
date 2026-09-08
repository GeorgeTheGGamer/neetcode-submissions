# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 1 Indexed
        values = []

        queue = collections.deque()
        queue.append(root)

        while queue:
            qlen = len(queue)
            for _ in range(qlen):
                current_node = queue.popleft()
                if current_node:
                    values.append(current_node.val)
                    queue.append(current_node.left)
                    queue.append(current_node.right)
        
        values.sort()
        return values[k-1]
        