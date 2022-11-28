import os
import sys

test_dir = os.path.dirname(__file__)
code_dir = os.path.normpath(test_dir + "/../problem_set_1")

sys.path.append(code_dir)

import unittest

from problem_set_1 import ps1a as p

class Test_ps1a(unittest.TestCase):
    def setUp(self) -> None:
        self.cows = p.load_cows(code_dir + "/test_cow_data.txt")
    
    def test_load_cows(self):
        self.assertEqual(self.cows, {"Maggie" : 3, "Herman" : 7, "Betsy" : 9})

    def test_greedy_cow_transport_simple(self):
        self.assertEqual(p.greedy_cow_transport(self.cows), [["Maggie", "Herman"], ["Betsy"]])

    def test_simple_brute_force(self):
        result = p.brute_force_cow_transport(self.cows)
        self.assertTrue(["Maggie", "Herman"] in result and ["Betsy"] in result)
        
