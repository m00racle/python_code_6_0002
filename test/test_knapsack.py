import os
import sys

test_dir = os.path.dirname(__file__)
code_dir = os.path.normpath(test_dir + "/../lec_1-intro")

sys.path.append(code_dir)

import unittest

import knapsack as kg


class Test_knapsack(unittest.TestCase):
    def setUp(self) -> None:
        self.bagger = kg.Item('bagger', 10, 5)
        self.items = kg.buildItems()
    
    def test_get_name_from_item(self):
        self.assertEqual(self.bagger.getName(), 'bagger')
    
    def test_get_value_float_from_item(self):
        """ test if the function returns value float of the item """
        self.assertTrue(type(self.bagger.getValue()) is float)
    
    def test_get_value_from_item(self):
        self.assertEqual(self.bagger.getValue(), 10.0)
    
    def test_get_weight_float_from_item(self):
        self.assertTrue(type(self.bagger.getWeight()) is float)

    def test_get_weight_from_item(self):
        self.assertEqual(self.bagger.getWeight(), 5.0)

    def test_value_returns_float_value(self):
        self.assertTrue(type(kg.value(self.bagger)) is float, "returns type not float!")
        self.assertEqual(kg.value(self.bagger), 10.0, "returned value is wrong")

    def test_value_return_from_weight_function(self):
        self.assertTrue(type(kg.weightInverse(self.bagger)) is float, "inverse weight returns wrong type")
        self.assertEqual(kg.weightInverse(self.bagger), 1/5, "inverse weight value is wrong")
    
    def test_value_return_from_density_function(self):
        self.assertTrue(type(kg.density(self.bagger)) is float, "density type is wrong")
        self.assertEqual(kg.density(self.bagger), 10/5, "densiti VALUE is wrong")

    def test_build_items(self):
        """ build all listed items into list of items.... """
        self.assertEqual(len(self.items), 6, "list SIZE is WRONG")
        self.assertEqual(str(self.items[2]), "<radio, 20.0, 4.0>", "the list SEQUENCE is WRONG")

    # integration testing
    def test_greedy_by_value(self):
        (self.taken, self.totalValue) = kg.greedy(self.items, 20.0, kg.value)
        self.assertEqual(len(self.taken), 1, "taken LIST SIZE is Wrong")
        self.assertEqual(str(self.taken[0]), "<computer, 200.0, 20.0>", "the CONTENT of the taken list is WORNG")
        self.assertEqual(self.totalValue, 200.0, "the total value of the taken is WRONG")
    
    def test_greedy_by_inverse_weight(self):
        (self.taken, self.totalValue) = kg.greedy(self.items, 20, kg.weightInverse)
        self.assertEqual(len(self.taken), 4, "taken LIST SIZE is Wrong")
        self.assertEqual(str(self.taken[2]), "<radio, 20.0, 4.0>", "the CONTENT of the taken list is WORNG")
        self.assertEqual(self.totalValue, 170.0, "the total value of the taken is WRONG")

    def test_greedy_by_density(self):
        (self.taken, self.totalValue) = kg.greedy(self.items, 20.0, kg.density)
        self.assertEqual(len(self.taken), 4, "taken LIST SIZE is Wrong")
        self.assertEqual(str(self.taken[1]), "<clock, 175.0, 10.0>", "the CONTENT of the taken list is WORNG")
        self.assertEqual(self.totalValue, 255.0, "the total value of the taken is WRONG")

    def test_generate_binary_reps_digits(self):
        self.assertEqual(kg.getBinaryRep(0,4), '0000', "4 digits binary rep for 0 is WRONG")
        self.assertEqual(kg.getBinaryRep(1,6), '000001', "6 digits binary rep for 1 is WRONG")
        self.assertEqual(kg.getBinaryRep(15,8), '00001111', "8 digits binary rep for 15 is WRONG")

    def test_generate_binary_larger_than_digits_invoke_error(self):
        with self.assertRaises(ValueError) as cm:
            kg.getBinaryRep(8, 3)
        
        self.assertTrue("not enough digits" in cm.exception)

    def test_generate_binary_all_1s(self):
        self.assertEqual(kg.getBinaryRep(15,4), "1111", "4 digits binary reps for 15 is WRONG")
        

    def test_generating_powerset_from_simple_list(self):
        # preps
        startList = [1,2]
        self.assertEqual(kg.genPowerSet(startList), [[], [1], [2], [1,2]])

if __name__ == '__main__':
    unittest.main()