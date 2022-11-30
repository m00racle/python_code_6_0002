import os, sys, unittest

test_dir = os.path.dirname(__file__)
code_dir = os.path.normpath(test_dir + "/../lec_1-intro")

sys.path.append(code_dir)

import gcd as g

class Test_gcd(unittest.TestCase):
    
    def setUp(self) -> None:
        return super().setUp()

    def test_loo_gcd(self):
        self.assertEqual(g.hcfLoop(1220, 516), 4)

    def test_loop_gcd_commutative(self):
        self.assertEqual(g.hcfLoop(516, 1220), 4)
    
    def test_resurs_gcd_(self):
        self.assertEqual(g.hcfRecurs(1220, 516), 4)
    
    def test_recurs_gcd_commutative(self):
        self.assertEqual(g.hcfRecurs(516, 1220), 4)
    
    def test_lcm_returns(self):
        self.assertEqual(g.lcm(1220, 516), 157380)
    
    def test_lcm_commutative(self):
        self.assertFalse(g.lcm(516, 1220) == 0)
        self.assertEqual(g.lcm(516, 1220), g.lcm(1220, 516))
