# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        dummyNode.next = head
        currNode = head
        prevNode = dummyNode
        while currNode != None and currNode.next != None:
            nodeA, nodeB = currNode, currNode.next
            nextNode = nodeB.next
            nodeB.next = nodeA
            nodeA.next = nextNode
            prevNode.next = nodeB
            prevNode = nodeA
            currNode = nextNode

        return dummyNode.next