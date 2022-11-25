# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        currNode = head
        prevNode = None

        while currNode != None:
            prevNode = currNode
            currNode = currNode.next
            while currNode!=None and prevNode.val == currNode.val:
                prevNode.next = currNode.next
                currNode = currNode.next
        return head

