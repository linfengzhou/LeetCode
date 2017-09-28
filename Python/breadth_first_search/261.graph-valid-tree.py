class Solution:
    """
    @param: n: An integer
    @param: edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # write your code here
        if n == 0:
            return False
        if len(edges) != n - 1:
            return False
        graph = self.init_graph(n, edges)
        target_nodes = set([0])
        queue = [0]
        while len(queue) != 0:
            node = queue.pop()
            total_target = graph.get(node)
            if not total_target:
                continue
            for target in total_target:
                if target not in target_nodes:
                    target_nodes.add(target)
                    queue.append(target)
        return len(target_nodes) == n

    def init_graph(self, n, edges):
        res = {}
        for edge in edges:
            node_a = edge[0]
            node_b = edge[1]
            if node_a not in res:
                res[node_a] = set([node_b])
            if node_b not in res:
                res[node_b] = set([node_a])
            res[node_a].add(node_b)
            res[node_b].add(node_a)
        return res
