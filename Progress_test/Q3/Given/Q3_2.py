class Q3_2:
    def f2(self, a, start): 
        #a is the adjacency matrix representing the given graph
        # start is a starting point 
        from Graph import Graph
        Graph = Graph(a)
        Graph.f2(start)
        