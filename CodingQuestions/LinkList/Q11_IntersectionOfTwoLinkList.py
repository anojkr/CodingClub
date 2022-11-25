# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def getSize(self, head):
        currNode = head
        count = 0
        while currNode != None:
            currNode = currNode.next
            count += 1
        return count

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        sizeA = self.getSize(headA)
        sizeB = self.getSize(headB)
        diffSize = abs(sizeA - sizeB)

        if sizeA >= sizeB:
            currNodeA = headA
            currNodeB = headB
        else:
            currNodeA = headB
            currNodeB = headA

        while currNodeA != None and diffSize > 0:
            currNodeA = currNodeA.next
            diffSize -= 1

        while currNodeA != None:
            if currNodeA == currNodeB:
                return currNodeA
            currNodeA = currNodeA.next
            currNodeB = currNodeB.next
