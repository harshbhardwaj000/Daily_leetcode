# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        while head and head.val == val:
            head=head.next
        t1=head
        while t1 and t1.next:
            if t1.next.val==val:
                t1.next=t1.next.next
            else:
                t1=t1.next
        return head

        