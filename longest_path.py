from collections import defaultdict

class Graph:
    def __init__ (self, vertices):
        self.V = vertices # No of vertices
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v,w):
        self.graph[u].append((v,w))

    def topologicalSortUtil(self,v,visited,stack):
        visited[v] = True

        if v in self.graph.keys():
            for node, weight in self.graph[v]:
                if visited[node] == False:
                    self.topologicalSortUtil(node, visited, stack)
        
        stack.append(v)
    
    def shortestPath(self, s, t):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(s, visited, stack)
        
        dist = [float("Inf")] * (self.V)
        parent = [0] * (self.V)
        
        dist[s] = 0
        stack.reverse()
        for val in stack:
            for edge in self.graph[val]:
                end, weight = edge
                if dist[end] > dist[val] + weight:
                    dist[end] = dist[val] + weight
                    parent[end] = val

       
        def helper(next):
            if next == s:
                print(s,end="->")
                return
            helper(parent[next])
            if next == t:
                print(t)
                return
            print(next, end="->")
            
        helper(t)
        print("")
    
    def longestPath(self, s, t):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(s, visited, stack)
        
        dist = [float("-Inf")] * (self.V)
        parent = [0] * (self.V)
        
        dist[s] = 0
        stack.reverse()
        for val in stack:
            for edge in self.graph[val]:
                end, weight = edge
                if dist[end] < dist[val] + weight:
                    dist[end] = dist[val] + weight
                    parent[end] = val

       
        def helper(next):
            if next == s:
                print(s,end="->")
                return
            helper(parent[next])
            if next == t:
                print(t)
                return
            print(next, end="->")
            
        helper(t)
        print("")

# longest increasing subsequence
sequence = [1,4,5,2,3,7,5,9,1,12,14,5,5,5,5,55,56,49]
g = Graph(len(sequence) + 2)
for num in range(len(sequence)):
    for j in range(num+1, len(sequence)):
        if sequence[num] <= sequence[j]:
            w = 1
        else:
            w = -1
        g.addEdge(num, j, w)
    
    g.addEdge(len(sequence), num, 0)
    g.addEdge(num, len(sequence) + 1, 0)

print(g.graph)
g.longestPath(len(sequence),len(sequence) + 1)