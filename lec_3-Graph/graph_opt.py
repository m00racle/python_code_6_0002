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

class Graph(Digraph):
    """  
    class represent Graph
    sub-class of Digraph
    """
    