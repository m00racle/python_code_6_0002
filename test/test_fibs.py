import os, sys, unittest

test_dir = os.path.dirname(__file__)
code_dir = os.path.normpath(test_dir + '/../lec_2-Optimization')

sys.path.append(code_dir)

import fibs as f

class Test_fibs(unittest.TestCase):

    def setUp(self) -> None:
        self.memo = {'calls' : 0}
    
    def test_fibs_for_0_returns_0_depth_0(self):
        res = f.fibs(0, self.memo)
        self.assertEqual(res, [0, {'calls':0}])
    
    def test_fibs_for_1_returns_1_depth_0(self):
        self.assertEqual(f.fibs(1, self.memo), [1, {'calls':0}])

    def test_fib_for_2_returns_1_depth_2(self):
        self.assertEqual(f.fibs(2, self.memo), [1,{'calls':2}])
    def test_fib_for_6_returns_8(self):
        fibo = f.fibs(6, self.memo)
        self.assertEqual(fibo, [8, {'calls':24}])

    