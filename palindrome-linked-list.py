# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val  int   
#         self.next = next   address  
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        
        left = head
        right = head
        
        while(right is not None and right.next is not None):
            left = left.next
            right = right.next.next
            
        right = self.reverseList(left)
        left = head
        
        while(left):
            if left.val != right.val:
                return False
            if left.next==right or right.next==left:
                left=None
            else:   
                left = left.next
                right = right.next
            
        return True
    
    def reverseList(self, node):
        current = node
        previous = None
        while(current):
            currentNext = current.next  
            current.next = previous  
            previous = current
            current = currentNext
            
        return previous
