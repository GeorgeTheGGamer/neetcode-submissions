# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # Reverse the right side
        current = slow.next
        prev = slow.next = None

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp


        # Reorder
        start = head
        end = prev          # This is since the linkedlist is going in the opposite direction

        while start and end:
            tmp1 = start.next
            tmp2 = end.next
            start.next = end
            end.next = tmp1
            start = tmp1
            end = tmp2


    

        
        
        
        
        


        
        





            
            

        





        