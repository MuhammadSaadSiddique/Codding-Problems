# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find beginning occurence of k by moving k-1 stpes from head since list is 1 indexed
        start_k = head
        count = k-1
        while(count):
            start_k = start_k.next
            count-=1
        
        # find ending occurence of k by 2 pointer apporach 
        end_k,cursor = head,start_k
        while(cursor.next):
            cursor = cursor.next
            end_k = end_k.next
            
        # swap
        start_k.val,end_k.val = end_k.val,start_k.val
        
        return head