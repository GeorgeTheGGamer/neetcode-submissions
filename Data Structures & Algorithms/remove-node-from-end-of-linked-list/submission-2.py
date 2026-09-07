# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        N=0         # Length of linked list
        curr = head

        while curr:
            N += 1
            curr = curr.next
        
        # Remove nth from the end of list
        removeIndex = N-n
        if removeIndex == 0:
            return head.next
        
        curr = head
        for i in range(N-1):
            if removeIndex == (i+1):
                 curr.next = curr.next.next
                 break      # No need to run through anymore
            curr = curr.next
        

        return head
        



        


        