# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return 
        hasCycle = False
        slow, fast = head, head
        while fast and  fast.next !=None:
            slow= slow.next
            fast=fast.next.next
            if slow==fast:
                hasCycle = True
                break
        
        if not hasCycle:
            return None
        
        slow =head
        while slow !=fast:
            slow=slow.next
            fast=fast.next
           
        return slow
        