"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        
        # Create weaved list, no connection
        while curr:
            copy = Node(curr.val, curr.next)
            curr.next = copy
            curr = copy.next
        old = head
        
        # Connect random
        while old:
            copy = old.next
            copy.random = old.random.next if old.random else None
            old = copy.next
        cloneHead = head.next if head else None
        
        # Connect next and Unweaved list
        old = head
        while old:
            copy = old.next
            nextOld = copy.next
            copy.next = nextOld.next if nextOld else None
            old.next = nextOld
            old = old.next

        return cloneHead