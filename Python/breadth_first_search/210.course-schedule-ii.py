class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # count indegree and init graph
        edges = [[] for i in range(numCourses)]
        degrees = [0 for i in range(numCourses)]

        for i, j in prerequisites:
            edges[preq[j]].append(i)
            degrees[i] += 1

        queue = []
        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)
        res = []
        while len(queue) != 0:
            node = queue.pop(0)
            res.append(node)

            for x in edges[node]:
                degrees[x] -= 1
                if degrees[x] == 0:
                    queue.append(x)

        if len(res) == numCourses:
            return res
        return 【】
