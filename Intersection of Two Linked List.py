# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA, curB = headA, headB
        while curA and curB:
            curA = curA.next
            curB = curB.next
        while curA:
            headA = headA.next
            curA = curA.next
        while curB:
            headB = headB.next
            curB = curB.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
