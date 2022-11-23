# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def getSize(self, head):
        currNode = head
        count = 0
        while currNode != None:
            currNode = currNode.next
            count += 1
        return count

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head

        size = self.getSize(head)
        k = k % size

        if k == 0 or k == size:
            return head

        currNode = head
        count = abs(size - k)

        while currNode != None and count > 0:
            prevNode = currNode
            currNode = currNode.next
            count -= 1
        prevNode.next = None

        newHead = currNode
        while currNode != None and currNode.next != None:
            currNode = currNode.next
        currNode.next = head
        return newHead