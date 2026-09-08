# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queue1 = collections.deque()
        queue2 = collections.deque()
        queue1.append(p)
        queue2.append(q)


        while queue1 and queue2:
            p_length = len(queue1)
            q_length = len(queue2)

            if p_length != q_length:
                return False

            for _ in range(p_length):
                p_node = queue1.popleft()
                q_node = queue2.popleft()

                if p_node and q_node and p_node.val == q_node.val:       
                    queue1.append(p_node.left)
                    queue1.append(p_node.right)
                    queue2.append(q_node.left)
                    queue2.append(q_node.right)
                elif not(p_node) and not(q_node):
                    continue
                else:
                    return False
        

        return True
        