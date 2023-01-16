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
    