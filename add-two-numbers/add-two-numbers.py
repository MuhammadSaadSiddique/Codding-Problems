# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2,c=0):
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10 ) 
        
        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
        return ret
        '''dl1=l1
        dl2=l2
        dumy=ListNode(0)
        temp=dumy
        c=0
        while (dl1.next!=None or dl2.next!=None or c!=0):
            if dl1.next!=None:
                v1=dl1.val
                dl1=dl1.next
            else:
                v1=dl1.val
            if dl2.next!=None:
                v2=dl2.val
                dl2=dl2.next
            else:
                v2=dl2.val
            v=v1+v2+c
            c=v/10
            v=v%10
            print(v)
            ret=ListNode(v)
            if temp!=None:
                temp.next=ret
                temp=ret
            else:
                temp=ret
                dumy=temp
                
