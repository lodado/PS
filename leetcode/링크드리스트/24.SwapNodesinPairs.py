# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        start = ListNode(None, None)
        cursor = start
        
        while(head and head.next):
            
            first = head
            second = head.next
            nextNode = head.next.next
            
            cursor.next = second
            second.next = first
            first.next = None
            head = nextNode
            cursor = first
            
        if(head):
            cursor.next = head
            
        return start.next
