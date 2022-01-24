# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.prev = None


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        header = head
        cursor = None
        
        while(head):
            head.prev = cursor
            cursor = head
            head = head.next

        while(header and cursor):
            if(cursor.val != header.val):
                return False
            header = header.next
            cursor = cursor.prev
        return True
