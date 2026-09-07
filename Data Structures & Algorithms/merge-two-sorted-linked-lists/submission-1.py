# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = tail = ListNode()        # These point to the start + end of linked list

        while list1 and list2:

            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next      # Increment to next node in this list
            else:
                tail.next = list2       # Increment to next node in this list
                list2 = list2.next
            tail = tail.next            # Increment to next node in tail
        

        if list1 and not(list2):
            tail.next = list1
        else:
            tail.next = list2
        
        return head.next
        