import collections


class Solution:
    vis = set()
    flag = False

    def dfs(self, graph, source, destination):
        if source == destination:
            self.flag = True

        self.vis.add(source)
        neighbour = graph.get(source)
        if neighbour != None:
            for ngh in neighbour.keys():
                if ngh not in self.vis:
                    self.dfs(graph, ngh, destination)

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.vis = set()
        self.flag = False
        graph = collections.defaultdict(dict)
        for src, des in edges:
            graph[src][des] = True
            graph[des][src] = True
        self.dfs(graph, source, destination)
        return self.flag
