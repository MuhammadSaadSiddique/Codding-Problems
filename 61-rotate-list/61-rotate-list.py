# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k:
            return head
        # capture the length of the list
        copy = head
        size = 1
        while copy.next:
            size+=1
            copy = copy.next
        # sometimes k > size, in such case perform modulo to reduce the value
        k = k%size if k>=size else k
        # k = 0 means performing rotation will bring same arrangement, hence return head
        if k==0:
            return head
        else:
            copy.next = head
        
        # move to a point where we need to cut the link
        ctr = 1
        while ctr<size-k:
            head = head.next
            ctr+=1
        # store the value to return and remove the link
        temp = head.next
        head.next = None
        return temp