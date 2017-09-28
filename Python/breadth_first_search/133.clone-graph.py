# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    def cloneGraph(self, node):
        root = node
        if not node:
            return node

        # get all nodes using bfs
        res = self.getNodes(node)

        # copy nodes, store the old-new mapping info in a hash map
        mapping = {}
        for node in res:
            mapping[node] = UndirectedGraphNode(node.label)

        # copy edges
        for node in res:
            new_node = mapping.get(node)
            for neighbor in node.neighbors:
                new_neighbor = mapping.get(neighbor)
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

    def getNodes(self, node):
        queue = [node]
        result = set([node])
        while len(queue) != 0:
            node = queue.pop()
            for neighbor in node.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    queue.append(neighbor)
        return result
