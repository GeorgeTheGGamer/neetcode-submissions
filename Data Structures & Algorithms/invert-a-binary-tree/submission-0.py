# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        stack.append(root)

        while stack:
            current_node = stack.pop()
            if current_node:
                temp = current_node.left
                current_node.left = current_node.right
                current_node.right = temp
                
            if current_node and current_node.left:
                stack.append(current_node.left)
            if current_node and current_node.right:
                stack.append(current_node.right)
        
        return root
        