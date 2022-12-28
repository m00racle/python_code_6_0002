import sys, os, unittest

test_dir = os.path.dirname(__file__)
code_dir = os.path.normpath(test_dir + "/../lec_3-Graph")
sys.path.append(code_dir)

from graph_opt import Node, Edge, WeightedEdge, Graph, Digraph

class TestGraphModel(unittest.TestCase):
    """  
    test scenarios for Graph and Digraph with their whole components
    """
    def setUp(self) -> None:
        self.nodeA = Node('A')
        self.nodeB = Node('B')

    def test_make_edge(self):
        """  
        test making edge from node A to node B
        """
        edge1 = Edge(self.nodeA, self.nodeB)
        # assert
        # assert have the correct source
        self.assertEqual(edge1.getSource(), self.nodeA, "The edge source is wrong")
        # assert have the correct destination
        self.assertEqual(edge1.getDestination(), self.nodeB, "The edge destination is wrong")
        # assert have the correct print out
        self.assertEqual(str(edge1), "A->B", "The edge is wrong")
    
    def test_make_weighted_edge_with_default_weight(self):
        """  
        test making weighted edge with weight = 1.0 (default)
        """
        wEdge_1 = WeightedEdge(self.nodeA, self.nodeB)
        # assert
        # assert have the correct source
        self.assertEqual(wEdge_1.getSource(), self.nodeA, "The weighted edge (default) source is wrong")
        # assert have the correct destination
        self.assertEqual(wEdge_1.getDestination(), self.nodeB, "The weighted edge (default) destination is wrong")
        # assert have the correct weight
        self.assertEqual(wEdge_1.getWeight(), 1.0, "The weighted edge (default) weight is wrong")
        # assert have the correct print out
        self.assertEqual(str(wEdge_1), "A->(1.0)B", "The default weighted edge is wrong")

    def test_make_weighted_edge(self):
        """  
        test making weighted edge with weight != 1.0
        """
        wEdge_2 = WeightedEdge(self.nodeA, self.nodeB, 2.75)
        # assert
        # assert have the correct source
        self.assertEqual(wEdge_2.getSource(), self.nodeA, "The weighted edge source is wrong")
        # assert have the correct destination
        self.assertEqual(wEdge_2.getDestination(), self.nodeB, "The weighted edge destination is wrong")
        # assert have the correct weight
        self.assertEqual(wEdge_2.getWeight(), 2.75, "The weighted edge weight is wrong")
        # assert have the correct print out
        self.assertEqual(str(wEdge_2), "A->(2.75)B", "The weighted edge is wrong")