import os, sys, unittest

test_dir = os.path.dirname(__file__)
code_dir = os.path.normpath(test_dir + "/../lec_2-Optimization")

sys.path.append(code_dir)

import gen_knapsack as gk

class TestGenClassKnapsack(unittest.TestCase):
    def setUp(self) -> None:
        self.d = gk.Thing("default", 95, 11)
        self.b = gk.Thing("custom", 99, 15, 'price', 'weight')
    
    def test_print_default_thing_instance(self):
        self.assertEqual(str(self.d), "<default; value: 95.0; cost: 11.0>")
    
    def test_print_custom_thing_instance(self):
        self.assertEqual(str(self.b), "<custom; price: 99.0; weight: 15.0>")
    
    def test_get_cost_name_default(self):
        self.assertEqual(self.d.getCostName(), 'cost')

    def test_get_cost_name_custom(self):
        self.assertEqual(self.b.getCostName(), 'weight')
    
    def test_get_value_name_default(self):
        self.assertEqual(self.d.getValueName(), 'value')
    
    def test_get_value_name_custom(self):
        self.assertEqual(self.b.getValueName(), 'price')

    def test_getName_default_returns_default(self):
        self.assertEqual(self.d.getName(), 'default')

    def test_get_name_custom_returns_string_custom(self):
        self.assertEqual(self.b.getName(), 'custom')

    def test_get_value_default_returns_correct_float_amount(self):
        self.assertTrue(type(self.d.getValue()) is float, "getValue FAILED to return float number")
        self.assertEqual(self.d.getValue(), 95.0, "getValue returns WRONG VALUE")

    def test_get_cost_custom_returns_correct_float_amount(self):
        self.assertTrue(type(self.b.getCost()) is float, "getCost FAILED to return float number")
        self.assertEqual(self.b.getCost(), 15.0, "getCost returns WRONG VALUE")

    