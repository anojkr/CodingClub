import collections

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer

    def dfs(self, graph, startNode, desNode):
        stack = []
        vis = set()
        stack.append(startNode)
        vis.add(startNode)

        while stack:
            node = stack.pop()
            if node == desNode:
                return 1
            adjacentNode = graph.get(node)
            if adjacentNode != None:
                for adjNode in adjacentNode.keys():
                    if adjNode not in vis:
                        stack.append(adjNode)
                        vis.add(adjNode)
        return 0

    def solve(self, A, B):
        graph = collections.defaultdict(dict)
        for src, des in B:
            graph[src][des] = True
        return self.dfs(graph, 1, A)
