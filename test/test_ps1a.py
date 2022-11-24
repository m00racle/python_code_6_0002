import os
import sys

test_dir = os.path.dirname(__file__)
code_dir = os.path.normpath(test_dir + "/../problem_set_1")

sys.path.append(code_dir)

import unittest

from problem_set_1 import ps1a as p

class Test_ps1a(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_load_cows(self):
        self.assertEqual(p.load_cows(code_dir + "/test_cow_data.txt"), {"Maggie" : 3, "Herman" : 7, "Betsy" : 9})