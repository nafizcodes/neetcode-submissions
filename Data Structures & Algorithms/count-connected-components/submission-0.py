class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(node):
            if node in visited:
                return 0

            visited.add(node)
            for neighbor in adjlist[node]:
                dfs(neighbor)
            return 1

        adjlist = [[] for i in range(n)]

        for nodeA, nodeB in edges:
            adjlist[nodeA].append(nodeB)
            adjlist[nodeB].append(nodeA)
        
        visited = set()

        sum = 0
        for node in range(n):
            sum += dfs(node)
            
        return sum

        # [[1], [0,2], [1], [4], [3]]

