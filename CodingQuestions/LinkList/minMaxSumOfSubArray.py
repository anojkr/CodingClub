import collections


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        arr = A
        windowSize = B

        maxQ = collections.deque()
        maxAns = 0
        for i in range(0, N):
            while len(maxQ) > 0 and i - maxQ[0] >= B:
                maxQ.popleft()
            while len(maxQ) > 0 and arr[maxQ[-1]] <= arr[i]:
                maxQ.pop()
            maxQ.append(i)
            if i >= B - 1:
                maxAns += arr[maxQ[0]]

        minQ = collections.deque()
        minAns = 0
        for i in range(0, N):
            while len(minQ) > 0 and i - minQ[0] >= B:
                minQ.popleft()
            while len(minQ) > 0 and arr[minQ[-1]] >= arr[i]:
                minQ.pop()
            minQ.append(i)
            if i >= B - 1:
                minAns += arr[minQ[0]]
        # print(minQ, minAns)

        return (minAns + maxAns) % 1000000007
