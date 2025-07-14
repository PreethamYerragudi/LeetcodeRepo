from collections import deque


class Solution(object):

    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        """
        U:
            I: two lists representing red connections and blue connections and an integer that represents the number of nodes
            O: A list of the length of the shortest path to get to each nodes
            C: redEdges[i].length == blueEdges[j].length == 2
            E: if there are no red or blue edges -> return a list with just the value 0 and -1 for all other nodes
        P:
        """
        seen = set()
        ans = [-1] * n
        ans[0] = 0
        if not redEdges and not blueEdges:
            return ans
        connections = {"Red": {}, "Blue": {}}

        for connection in redEdges:
            i, j = connection[0], connection[1]
            if not connections["Red"].get(i, None):
                connections["Red"][i] = []
            connections["Red"][i].append(j)

        for connection in blueEdges:
            i, j = connection[0], connection[1]
            if not connections["Blue"].get(i, None):
                connections["Blue"][i] = []
            connections["Blue"][i].append(j)
        #Red edge is true, and blue edge is false
        q = deque([(0, True, 0)])
        q.append((0, False, 0))
        seen.add((0, True))
        seen.add((0, False))
        while q:
            node, red, length = q.popleft()
            if ans[node] == -1:
                ans[node] = length
            if red:
                for connection in connections["Blue"].get(node, []):
                    if (connection, False) not in seen:
                        q.append((connection, False, length + 1))
                        seen.add((connection, False))
            else:
                for connection in connections["Red"].get(node, []):
                    if (connection, True) not in seen:
                        q.append((connection, True, length + 1))
                        seen.add((connection, True))
        return ans
