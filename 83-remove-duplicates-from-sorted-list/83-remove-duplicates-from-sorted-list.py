# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        temp_node = head
        while temp_node:
            if temp_node.next:
                if temp_node.val == temp_node.next.val:
                    temp_node.next = temp_node.next.next
                    continue
            temp_node = temp_node.next
        return head