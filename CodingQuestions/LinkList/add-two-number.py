# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        head = ListNode(-1)
        curr = head
        while l1 != None or l2!=None:
            a = l1.val if l1 != None else 0
            b = l2.val if l2 != None else 0
            sumNum = a + b + carry
            num = sumNum%10
            carry = sumNum//10
            curr.next = ListNode(num)
            curr = curr.next
            if l1!=None:
                l1 = l1.next
            if l2!=None:
                l2 = l2.next
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next


