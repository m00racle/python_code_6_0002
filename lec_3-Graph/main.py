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

def main():
    runDFS()

if __name__ == "__main__":
    main()