"""  
Code from the Handgbook 17.2 
"""

class Node(object):
    """  
    class to represent Node
    """
    def __init__(self, name) -> None:
        self.name = name
    
    def getName(self):
        return self.name

    def __str__(self) -> str:
        return self.name

class Edge(object):
    """  
    class to represent Edge in graph 
    """

class WeightedEdge(Edge):
    """  
    class represent Weighted Edge in graph
    sub-class of Edge
    """

class Digraph(object):
    """  
    class represent directed graph 
    """

class Graph(Digraph):
    """  
    class represent Graph
    sub-class of Digraph
    """
    