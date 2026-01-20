# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        h1, h2 = list1, list2
        prevNode = ListNode(-1)
        prev = prevNode
        while h1 and h2:
            if h1.val<=h2.val :
                prev.next = h1
                h1= h1.next
            else:
                prev.next = h2
                h2= h2.next
            prev = prev.next
        if h1 is not None:
            prev.next =   h1
        else:
            prev.next =   h2
        return prevNode.next



        