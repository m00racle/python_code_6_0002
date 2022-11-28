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

    # Testing fastFibs() function

    def test_fastFibs_0_retuns_0_memo_0(self):
        res = f.fastFibs(0, self.memo)
        self.assertEqual(res, [0, self.memo])
    
    def test_fastFib_1_returns_1_memo_0(self):
        res = f.fastFibs(1, self.memo)
        self.assertEqual(res, [1, self.memo])
    
    def test_fatsFib_2_returns_1_memo_calls_2(self):
        fibo, mem = f.fastFibs(2, self.memo)
        self.assertEqual(fibo, 1, "FIBO NUMBER is wrong")
        self.assertEqual(mem['calls'], 2, "Call number is wrong")

    def test_fastFib_6_returns_fibo_8(self):
        fibo, mem = f.fastFibs(6, self.memo)
        self.assertEqual(fibo, 8)
        self.assertEqual(mem[2], 1)
        self.assertEqual(mem[3], 2)

    