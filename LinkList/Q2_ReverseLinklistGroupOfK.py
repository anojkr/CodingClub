# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def size(self, curr, k):
        count = 0
        while curr != None:
            curr = curr.next
            count += 1
        return count // k

    def reverse(self, head, k):
        currNode = head
        prevNode = None
        nextNode = None
        count = 0
        while count < k and currNode != None:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
            count += 1
        return prevNode, currNode

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        noOfGrp = self.size(head, k)
        dummyNode = ListNode(-1)
        dummyNode.next = head
        prevNode = dummyNode
        currNode = head

        while currNode != None and noOfGrp > 0:
            grpPrevNode, grpNextNode = self.reverse(currNode, k)
            prevNode.next = grpPrevNode
            prevNode = currNode
            currNode = grpNextNode
            noOfGrp -= 1

        prevNode.next = currNode
        return dummyNode.next



