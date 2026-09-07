# Iterative approach

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        # Always check if there is a root
        if not root:
            return None
        stack.append(root)


        while stack:
            current_node = stack.pop()
            temp = current_node.left
            current_node.left = current_node.right
            current_node.right = temp
                
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)
        
        return root
        