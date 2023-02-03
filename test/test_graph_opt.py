import sys, os, unittest, io

test_dir = os.path.dirname(__file__)
code_dir = os.path.normpath(test_dir + "/../lec_3-Graph")
sys.path.append(code_dir)

from graph_opt import Node, Edge, WeightedEdge, Graph, Digraph
import graph_opt as go

class TestNodeEdge(unittest.TestCase):
    """  
    test scenarios for Graph and Digraph with their whole components
    """
    def setUp(self) -> None:
        # make nodes passing node name in init
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

class TestGraphs(unittest.TestCase):
    """  
    Testing the Graph and Digraph
    """
    def setUp(self) -> None:
        """  
        Setting working grpah and digraph on Star model
        """
        self.A = Node('A')
        self.B = Node('B')
        self.D = Node('D')
        # add one more node for test purpose
        self.C = Node('C')

        # edge list:
        self.AB = Edge(self.A, self.B)
        self.BD = Edge(self.B, self.D)
        self.DA = Edge(self.D, self.A)
        self.AD = Edge(self.A, self.D)
        # add faux edges for test purposes
        self.DC = Edge(self.D, self.C)
        self.CD = Edge(self.C, self.D)
        # this edge is specific for graph class
        self.DB = Edge(self.D, self.B)

    def test_digraph_class(self):
        # Arrange
        digraph = Digraph()
        # add nodes to the digraph
        digraph.addNode(self.A)
        digraph.addNode(self.B)
        digraph.addNode(self.D)

        # add edges to the digraph
        digraph.addEdge(self.AB)
        digraph.addEdge(self.BD)
        digraph.addEdge(self.DA)
        digraph.addEdge(self.AD)

        # Assert tests:
        # test re-adding node A addNode(self.A) should raise ValueError('Duplicate node')
        with self.assertRaises(ValueError) as ve:
            digraph.addNode(self.A)
        self.assertEqual(str(ve.exception), "Duplicate node", "add node A should raise Value Error Duplicate node")

        # test adding edge CD addEdge(self.CD) should raise ValueError('Node not in graph')
        with self.assertRaises(ValueError) as ve:
            digraph.addEdge(self.CD)
        self.assertEqual(str(ve.exception), "Node not in graph", "add edge CD should raise Value Error Node not in graph")

        # test adding edge DC addEdge(self.DC) should raise ValueError('Node not in graph')
        with self.assertRaises(ValueError) as ve:
            digraph.addEdge(self.DC)
        self.assertEqual(str(ve.exception), "Node not in graph", "add node DC should raise Value Error Node not in graph")

         # test hasNode(self.A) should return TRUE
        self.assertTrue(digraph.hasNode(self.A), "has node A should return TRUE")

        # test hasNode(self.C) should return FALSE
        self.assertFalse(digraph.hasNode(self.C), "has node C should return FALSE")

        # test childrenOf(self.A) should return [self.B, self.D]
        self.assertEqual(digraph.childrenOf(self.A), [self.B, self.D], "children of A should be [B,D]")

        # test childrenOf(self.B) should return [self.D, ]
        self.assertEqual(digraph.childrenOf(self.B), [self.D,], "children of B is [D]")

        # test childrenOf(self.D) should return [self.A, ]
        self.assertEqual(digraph.childrenOf(self.D), [self.A,], "children of D should be [A]")

        # test childrenOf(self.C) should invoke ValueError('Node not in graph')
        with self.assertRaises(ValueError) as ve:
            digraph.childrenOf(self.C)
        self.assertEqual(str(ve.exception), "Node not in graph", "childrenOf C should raise Value Error Node not in graph")

        # test str(digraph) return A->B\nA->D\nB->D\nD->A
        self.assertEqual(str(digraph), "A->B\nA->D\nB->D\nD->A", "str function is WRONG")
    
    def test_graph_class(self):
        # Arrange
        graph = Graph()
        # add nodes to the digraph
        graph.addNode(self.A)
        graph.addNode(self.B)
        graph.addNode(self.D)

        # add edges to the digraph
        graph.addEdge(self.AB)
        graph.addEdge(self.BD)
        graph.addEdge(self.DA)
        graph.addEdge(self.AD)
        graph.addEdge(self.DB)

        # Assert tests:
        # test re-adding node A addNode(self.A) should raise ValueError('Duplicate node')
        with self.assertRaises(ValueError) as ve:
            graph.addNode(self.A)
        self.assertEqual(str(ve.exception), "Duplicate node", "add node A should raise Value Error Duplicate node")

        # test adding edge CD addEdge(self.CD) should raise ValueError('Node not in graph')
        with self.assertRaises(ValueError) as ve:
            graph.addEdge(self.CD)
        self.assertEqual(str(ve.exception), "Node not in graph", "add edge CD should raise Value Error Node not in graph")

        # test adding edge DC addEdge(self.DC) should raise ValueError('Node not in graph')
        with self.assertRaises(ValueError) as ve:
            graph.addEdge(self.DC)
        self.assertEqual(str(ve.exception), "Node not in graph", "add node DC should raise Value Error Node not in graph")

         # test hasNode(self.A) should return TRUE
        self.assertTrue(graph.hasNode(self.A), "has node A should return TRUE")

        # test hasNode(self.C) should return FALSE
        self.assertFalse(graph.hasNode(self.C), "has node C should return FALSE")

        # test childrenOf(self.A) should return [self.B, self.D, self.D]
        self.assertEqual(graph.childrenOf(self.A), [self.B, self.D, self.D], "children of A should be [B,D,D]")

        # test childrenOf(self.B) should return [self.A, self.D, self.D]
        self.assertEqual(graph.childrenOf(self.B), [self.A, self.D, self.D], "children of B is [A,D,D]")

        # test childrenOf(self.D) should return [self.B, self.A, self.A, self.B]
        self.assertEqual(graph.childrenOf(self.D), [self.B, self.A, self.A, self.B], "children of D should be [B, A, A, B]")

        # test childrenOf(self.C) should invoke ValueError('Node not in graph')
        with self.assertRaises(ValueError) as ve:
            graph.childrenOf(self.C)
        self.assertEqual(str(ve.exception), "Node not in graph", "childrenOf C should raise Value Error Node not in graph")

        # test str(graph) return A->B\nA->D\nA->D\nB->A\nB->D\nB->D\nD->B\nD->A\nD->A\nD->B
        self.assertEqual(str(graph), "A->B\nA->D\nA->D\nB->A\nB->D\nB->D\nD->B\nD->A\nD->A\nD->B", "graph str WRONG")

class TestOptMethod(unittest.TestCase):
    """  
    testing the Depth First Search method to find the optimal path from start to target. 
    """
    def setUp(self) -> None:
        """  
        Begin with setting the graph (Digraph) used for test case
        """
        self.d = Digraph()
        # create 6 nodes named 0 to 5:
        self.n = []
        for nom in range(6): self.n.append(Node(str(nom)))

        # put all nodes in self.d
        for nod in self.n:
            self.d.addNode(nod)

        # Now the hardest part: list all edges in the self.d
        self.d.addEdge(Edge(self.n[0], self.n[1]))
        self.d.addEdge(Edge(self.n[1], self.n[2]))
        self.d.addEdge(Edge(self.n[2], self.n[3]))
        self.d.addEdge(Edge(self.n[2], self.n[4]))
        self.d.addEdge(Edge(self.n[3], self.n[4]))
        self.d.addEdge(Edge(self.n[3], self.n[5]))
        self.d.addEdge(Edge(self.n[0], self.n[2]))
        self.d.addEdge(Edge(self.n[1], self.n[0]))
        self.d.addEdge(Edge(self.n[3], self.n[1]))
        self.d.addEdge(Edge(self.n[4], self.n[0]))


    def test_DFS_digraph_return_correct_list_of_nodes(self):
        """  
        Given g as Digraph with list of nodes N and list of Edges e
        Test using DFS it returns sp the most optimal path 
        path = list of nodes from start to end which has the shortest length.
        """
        result = go.DFS(self.d, self.n[0], self.n[5])
        # assert
        self.assertEqual(result, [self.n[0], self.n[2], self.n[3], self.n[5]])

    def test_DFS_verbose_print_out_correct_steps(self):
        """  
        Given the same case but in verbose mode the run should print out the corret 
        current path.
        """
        capOut = io.StringIO()
        sys.stdout = capOut
        
        printed = \
            "Current DFS path: 0\n" + \
            ">>> Current shortest path: None\n" +\
            "Current DFS path: 0->1\n" +\
            ">>> Current shortest path: None\n" +\
            "Current DFS path: 0->1->2\n" +\
            ">>> Current shortest path: None\n" +\
            "Current DFS path: 0->1->2->3\n" +\
            ">>> Current shortest path: None\n" +\
            "Current DFS path: 0->1->2->3->4\n" +\
            ">>> Current shortest path: None\n"+\
            "Current DFS path: 0->1->2->3->5\n"+\
            ">>> Current shortest path: None\n"+\
            "Current DFS path: 0->1->2->4\n"+\
            ">>> Current shortest path: 0->1->2->3->5\n"+\
            "Current DFS path: 0->2\n"+\
            ">>> Current shortest path: 0->1->2->3->5\n"+\
            "Current DFS path: 0->2->3\n"+\
            ">>> Current shortest path: 0->1->2->3->5\n"+\
            "Current DFS path: 0->2->3->4\n"+\
            ">>> Current shortest path: 0->1->2->3->5\n"+\
            "Current DFS path: 0->2->3->5\n"+\
            ">>> Current shortest path: 0->1->2->3->5\n"+\
            "Current DFS path: 0->2->3->1\n"+\
            ">>> Current shortest path: 0->2->3->5\n"+\
            "Current DFS path: 0->2->4\n"+\
            ">>> Current shortest path: 0->2->3->5\n"+\
            "Shortest path found by DFS: 0->2->3->5\n"

        # action
        # put the run here in verbose
        result = go.DFS(self.d, self.n[0], self.n[5], verbose=True)
        print(f'Shortest path found by DFS: {go.printPath(result)}')

        # capture
        sys.stdout = sys.__stdout__
        self.assertEqual(capOut.getvalue(), printed)

    def test_BFS_digraph_return_correct_list_of_nodes(self):
        """  
        Given g as Digraph with list of nodes N and list of Edges e
        Test using DFS it returns sp the most optimal path 
        path = list of nodes from start to end which has the shortest length.
        """
        result = go.BFS(self.d, self.n[0], self.n[5])
        # assert
        self.assertEqual(result, [self.n[0], self.n[2], self.n[3], self.n[5]])

    def test_BFS_verbose_print_out_correct_steps(self):
        """  
        Given the same case but in verbose mode the run should print out the corret 
        current path.
        """
        capOut = io.StringIO()
        sys.stdout = capOut
        
        printed = \
            "Current DFS path: 0\n" + \
            "Current DFS path: 0->1\n" + \
            "Current DFS path: 0->2\n" + \
            "Current DFS path: 0->1->2\n" + \
            "Current DFS path: 0->2->3\n" + \
            "Current DFS path: 0->2->4\n" + \
            "Current DFS path: 0->1->2->3\n" + \
            "Current DFS path: 0->1->2->4\n" + \
            "Current DFS path: 0->2->3->4\n" + \
            "Current DFS path: 0->2->3->5\n" + \
            "Shortest path found by DFS: 0->2->3->5\n"

        # action
        # put the run here in verbose
        result = go.BFS(self.d, self.n[0], self.n[5], verbose=True)
        print(f'Shortest path found by DFS: {go.printPath(result)}')

        # capture
        sys.stdout = sys.__stdout__
        self.assertEqual(capOut.getvalue(), printed)