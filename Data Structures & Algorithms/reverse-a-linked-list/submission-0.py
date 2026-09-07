# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        previous_node = None
        current = head

        while current:
            temp_next = current.next
            current.next = previous_node
            previous_node = current
            current = temp_next
        
        return previous_node
        

        