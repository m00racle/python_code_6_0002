import os
import sys

test_dir = os.path.dirname(__file__)
code_dir = os.path.normpath(test_dir + "/../problem_set_1")

sys.path.append(code_dir)

import unittest

from problem_set_1 import ps1a as p, ps1b as pb

class Test_ps1a(unittest.TestCase):
    def setUp(self) -> None:
        self.cows = p.load_cows(code_dir + "/test_cow_data.txt")
    
    def test_load_cows(self):
        self.assertEqual(self.cows, {"Maggie" : 3, "Herman" : 7, "Betsy" : 9})

    def test_greedy_cow_transport_simple(self):
        self.assertEqual(p.greedy_cow_transport(self.cows), [["Maggie", "Herman"], ["Betsy"]])

    def test_simple_brute_force(self):
        result = p.brute_force_cow_transport(self.cows)
        # self.assertTrue(["Maggie", "Herman"] in result and ["Betsy"] in result)
        self.assertTrue(result, [['Betsy'], ['Maggie', 'Herman']])
        
class Test_ps1b(unittest.TestCase):
    """  
    test case the ps1b Problem Set 1
    """
    def test_given_problem_ps1b_return_correct_amount(self):
        """  
        given target weight is 99
        eggs with weight 1, 5, 10, 25 
        assert that it return 9 as lifted amount
        """
        self.assertEqual(pb.dp_make_weight((1,5,10,25), 99), 9, "The number of lifted egg is wrong")