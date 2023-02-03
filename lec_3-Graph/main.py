import graph_opt as go
from graph_opt import Digraph, Edge, Node

def runDFS()->None:
    d = Digraph()
    # create 6 nodes named 0 to 5:
    n = []
    for nom in range(6): n.append(Node(str(nom)))

    # put all nodes in d
    for nod in n:
        d.addNode(nod)

    # Now the hardest part: list all edges in the d
    d.addEdge(Edge(n[0], n[1]))
    d.addEdge(Edge(n[1], n[2]))
    d.addEdge(Edge(n[2], n[3]))
    d.addEdge(Edge(n[2], n[4]))
    d.addEdge(Edge(n[3], n[4]))
    d.addEdge(Edge(n[3], n[5]))
    d.addEdge(Edge(n[0], n[2]))
    d.addEdge(Edge(n[1], n[0]))
    d.addEdge(Edge(n[3], n[1]))
    d.addEdge(Edge(n[4], n[0]))

    result = go.DFS(d, n[0], n[5], verbose=True)
    print(f'Shortest path found by DFS: {go.printPath(result)}')

def buildCityGraph(graphType):
    # creating digraph map
    g = graphType()
    # create cities as nodes
    cities = []
    boston = Node('Boston')
    cities.append(boston)
    providence = Node('Providence')
    cities.append(providence)
    new_york = Node('New York')
    cities.append(new_york)
    chicago = Node('Chicago')
    cities.append(chicago)
    denver = Node('Denver')
    cities.append(denver)
    phoenix = Node('Phoenix')
    cities.append(phoenix)
    los_angeles = Node('Los Angeles')
    cities.append(los_angeles)

    for city in cities:
        g.addNode(city)
    
    # input all edges in graph:
    g.addEdge(Edge(boston, providence))
    g.addEdge(Edge(boston, new_york))
    g.addEdge(Edge(providence, boston))
    g.addEdge(Edge(providence, new_york))
    g.addEdge(Edge(new_york, chicago))
    g.addEdge(Edge(chicago, denver))
    g.addEdge(Edge(chicago, phoenix))
    g.addEdge(Edge(denver, phoenix))
    g.addEdge(Edge(denver, new_york))
    g.addEdge(Edge(los_angeles, boston))

    return g

def testSP(source: str, destination: str):
    g = buildCityGraph(Digraph)
    print(f'\nSTART finding shortest path from {source} to {destination}')
    print(f'using DFS mehtod:')
    resultDfs = go.DFS(g, g.getNode(source), g.getNode(destination), verbose=True)
    if resultDfs != None:
        print(f'Shortes Path by DFS method: {go.printPath(resultDfs)}')
    else:
        print(f'DFS method failed to find path from {source} to {destination}')

    print(f'\nusing BFS method:')
    resultBFS = go.BFS(g,g.getNode(source), g.getNode(destination), verbose=True)
    if resultBFS != None:
        print(f'shortest Path by BFS method: {go.printPath(resultBFS)}')
    else:
        print(f'BFS method failed to find path from {source} to {destination}')

    

def main():
    testSP('Chicago', 'Boston')
    # this should not find any path!
    testSP('Boston', 'Phoenix')

if __name__ == "__main__":
    main()