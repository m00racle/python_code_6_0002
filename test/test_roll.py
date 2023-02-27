import os, sys, unittest

test_dir = os.path.dirname(__file__)
code_dir = os.path.normpath(test_dir + '/../lec_4_Stochastic')

sys.path.append(code_dir)

import roll_die as r

class Test_roll_die(unittest.TestCase):

    def test_roll_die_returns_1_to_6(self):
        self.assertTrue(r.rollDie() in range(1,7))

if __name__ == '__main__':
    unittest.main()