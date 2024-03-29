"""  
Code from the Handgbook 17.2 
"""

class Node(object):
    """  
    class to represent Node
    """
    def __init__(self, name) -> None:
        """  
        init args : name (str)
        """
        self.name = name
    
    def getName(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name

class Edge(object):
    """  
    class to represent Edge in graph
    once it set the source and destination it can't be modified! 
    """
    def __init__(self, source, destination) -> None:
        """  
        args : source (Node), destination (Node)
        """
        self.source = source
        self.destination = destination
    
    def getSource(self) -> Node:
        return self.source
    
    def getDestination(self) -> Node:
        return self.destination
    
    def __str__(self) -> str:
        return self.source.getName() + '->' + self.destination.getName()
class WeightedEdge(Edge):
    """  
    class represent Weighted Edge in graph
    sub-class of Edge
    """
    def __init__(self, source, destination, weight=1.0) -> None:
        """  
        same as init of Edge but add weight (float) as args
        """
        self.weight = weight
        super().__init__(source, destination)
    
    def getWeight(self) -> float:
        return self.weight

    def __str__(self) -> str:
        """  
        override the superclass str
        """
        return self.source.getName() + '->(' + str(self.weight) + ')' + self.destination.getName()

class Digraph(object):
    """  
    class represent directed graph 
    """
    def __init__(self) -> None:
        self.nodes = []
        self.edges = {}
    
    def addNode(self, node: Node) -> None:
        """  
        Given node : Node 
        append node to nodes list if has not or
        Raise Value Error
        Returns None
        """
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def addEdge(self, edge: Edge) -> None:
        """  
        Given edge : Edge
        append the edge into dict edges wiht source node as key and destination node as value
        or raise Value Error if node is not in list Nodes
        Returns None
        """
        source = edge.getSource()
        destination = edge.getDestination()
        if not(source in self.nodes and destination in self.nodes):
            raise ValueError('Node not in graph')
        # if the source and destination are listed in nodes then put them into dict edges
        self.edges[source].append(destination)

    def hasNode(self, node: Node) -> bool:
        """  
        Given node : Node
        Return TRUE if node is in nodes and FALSE otherwise
        """
        return node in self.nodes

    def getNode(self, name: str) -> Node:
        """  
        Given: name: str = name of the node
        Return: Node = if exist the node which has the name or riase NameError otherwise
        """
        for node in self.nodes:
            if node.getName() == name: return node
        
        # if no name match:
        raise NameError(name)

    def childrenOf(self, node: Node) -> list:
        """ 
        Given node : Node 
        if node in list nodes return list of node children
        else raise Value Error Node not in graph
        """
        if self.hasNode(node):
            return self.edges[node]
        else:
            raise ValueError("Node not in graph")

    def __str__(self) -> str:
        printed = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                printed = printed + src.getName() + '->' + dest.getName() + '\n'
        
        # remember to omit the \n in the last entry
        return printed[:-1] 

class Graph(Digraph):
    """  
    class represent Graph
    sub-class of Digraph
    """
    # override 
    def addEdge(self, edge: Edge) -> None:
        reverseEdge = Edge(edge.getDestination(), edge.getSource())
        super().addEdge(edge)
        super().addEdge(reverseEdge)

"""  
Methods of Graph optimizations
"""
def printPath(path: list)-> str:
    """  
    Given:
    path : list = list of nodes in a path

    Return : str = print (str) form of all nodes tied up together with ->
    """
    result = ''
    try:
        for i in range(len(path)):
            result = result + str(path[i])
            if i != len(path) - 1 :
                # add -> between them
                result = result + '->'
    except:
        return None

    return result

def DFS(graph: Digraph, start: Node, end: Node, path : list = [], shortest : list = None, verbose : bool = False) -> list:
    """  
    Given:
    graph : Digraph 
    start : Node = node designated as start of the path
    end : Node = node designated as end of the path
    path : list = list of taken path (default = [])
    shortest : list = list of shortest path (in terms of number of node elements) (default = None)

    Return: list = list of the shortest path from start Node to the end Node
    """
    # add the node (start) into the path list
    path = path + [start]

    if verbose : 
        # print the step by step path:
        print(f'Current DFS path: {printPath(path)}')
        print(f'>>> Current shortest path: {printPath(shortest)}')

    # base case
    if start == end : return path

    # recursive case:
    for child in graph.childrenOf(start) :
        # only pick children that is not yet in the path list to avoid circular edges:
        if child not in path :
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, child, end, path, shortest, verbose)
                if newPath != None:
                    shortest = newPath
    
    return shortest

def BFS(graph: Digraph, start: Node, end: Node, verbose=False):
    """  
    Given:
    graph: Digraph
    start: Node
    end: Node
    Find the shortest Node list from start to end

    Returns None
    """
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        # get and remove oldest element of the pathqueue
        tmpPath = pathQueue.pop(0)
        if verbose: print(f'Current BFS path: {printPath(tmpPath)}')
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        # check all children for the lastNode:
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    
    # if not path gets to end:
    return None