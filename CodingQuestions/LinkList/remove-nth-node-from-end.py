# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        nodePtr = head
        nodeCnt = 0
        while nodePtr != None:
            nodeCnt += 1
            nodePtr = nodePtr.next

        if nodeCnt == n:
            return head.next

        cnt = nodeCnt - n
        curr = head
        prev = None
        while cnt > 0:
            cnt -= 1
            prev = curr
            curr = curr.next

        prev.next = prev.next.next
        return head
