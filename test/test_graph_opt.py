import sys, os, unittest

test_dir = os.path.dirname(__file__)
code_dir = os.path.normpath(test_dir + "/../lec_3-Graph")
sys.path.append(code_dir)

from graph_opt import Node, Edge, WeightedEdge, Graph, Digraph

