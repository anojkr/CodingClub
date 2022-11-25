# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        N = len(lists)
        head = ListNode(-1)
        h = []
        for i in range(N):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
        curr = head
        while h:
            val, i = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
        return head.next
