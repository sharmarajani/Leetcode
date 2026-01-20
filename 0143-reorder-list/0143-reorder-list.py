# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        slow, fast = head, head

        # find middle of LL
        while fast and fast.next !=None:
            slow=slow.next
            fast=fast.next.next
        
        # reverse
        
        prev, curr = None, slow.next
        tmp = None
        slow.next =None
        fast = curr
        
        while curr:
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt
        # prev has second list      

        # merge 2 halves
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        


            
            

        