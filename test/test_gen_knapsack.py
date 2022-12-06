import os, sys, unittest

test_dir = os.path.dirname(__file__)
code_dir = os.path.normpath(test_dir + "/../lec_2-Optimization")

sys.path.append(code_dir)

import gen_knapsack as gk

class TestGenClassKnapsack(unittest.TestCase):
    def setUp(self) -> None:
        self.d = gk.Thing("default", 95, 11)
        self.b = gk.Thing("custom", 99, 15, value_name='price', cost_name='weight')
    
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

    def test_build_things_returns_list_of_correct_things(self):
        # prepare
        
        datas = {'clock' : [175, 10], 'painting' : [90, 9], 'radio' : [20, 4], 'vase' : [50, 1], 'book' : [10, 20], 'computer' : [200, 20]}
        itemList = gk.buildThings(datas, cost_custom = 'weight')
        result = []
        for item in itemList:
            result.append(str(item))
        
        compare = ['<clock; value: 175.0; weight: 10.0>', \
            '<painting; value: 90.0; weight: 9.0>',\
                '<radio; value: 20.0; weight: 4.0>',\
                    '<vase; value: 50.0; weight: 1.0>',\
                        '<book; value: 10.0; weight: 20.0>',\
                            '<computer; value: 200.0; weight: 20.0>']
        
        self.assertEqual(result, compare)

class TestGenGreedyKnapsack(unittest.TestCase):
    def setUp(self) -> None:
        self.datas = {'clock' : [175, 10], 'painting' : [90, 9], 'radio' : [20, 4], 'vase' : [50, 2], 'book' : [10, 1], 'computer' : [200, 20]}
        # self.s = samples of things to be tested
        self.s = gk.buildThings(self.datas, cost_custom='weight')

    def test_greedy_by_value_returns_correct_data_things(self):
        # prepare
        compare = ["<computer; value: 200.0; weight: 20.0>"]
        totalValue = 0
        totalWeight = 0
        result = []
        # action
        optByVal = gk.greedy(self.s, 20, lambda x : x.getValue())
        for thing in optByVal:
            result.append(str(thing))
            totalValue += thing.getValue()
            totalWeight += thing.getCost()
        
        # assert
        self.assertEqual(len(result), 1, "the amount of things is WRONG")
        self.assertEqual(result, compare, "the list of things is WRONG")
        self.assertTrue(totalWeight <= 20, "the total weight violate constraint")
        self.assertEqual(totalValue, 200.0, "the total value of things is wrong")
    
    def test_greedy_by_reverse_weight_returns_correct_data_things(self):
         # prepare
        compare = \
            ["<book; value: 10.0; weight: 1.0>",\
                "<vase; value: 50.0; weight: 2.0>",\
                    "<radio; value: 20.0; weight: 4.0>",\
                        "<painting; value: 90.0; weight: 9.0>"]
        totalValue = 0
        totalWeight = 0
        result = []
        # action
        optByWeight = gk.greedy(self.s, 20, lambda x : 1/x.getCost())
        for thing in optByWeight:
            result.append(str(thing))
            totalValue += thing.getValue()
            totalWeight += thing.getCost()
        
        # assert
        self.assertEqual(len(result), 4, "the amount of things is WRONG")
        self.assertEqual(result, compare, "the list of things is WRONG")
        self.assertTrue(totalWeight <= 20, "the total weight violate constraint")
        self.assertEqual(totalValue, 170.0, "the total value of things is wrong")

    def test_greedy_by_reverse_weight_must_equal_by_ascending_weight(self):
        optByWeight = gk.greedy(self.s, 20, lambda x : 1/x.getCost())
        optByAscWeight = gk.greedy(self.s, 20, lambda x : x.getCost(), descending=False)
        self.assertEqual(optByWeight, optByAscWeight)

    def test_greedy_by_density_returns_correct_data_things(self):
         # prepare
        compare = \
            ["<vase; value: 50.0; weight: 2.0>",\
                "<clock; value: 175.0; weight: 10.0>",\
                "<book; value: 10.0; weight: 1.0>",\
                    "<radio; value: 20.0; weight: 4.0>"]
        totalValue = 0
        totalWeight = 0
        result = []
        # action
        optByDensity = gk.greedy(self.s, 20, lambda x : x.getValue()/x.getCost())
        for thing in optByDensity:
            result.append(str(thing))
            totalValue += thing.getValue()
            totalWeight += thing.getCost()
        
        # assert
        self.assertEqual(len(result), 4, "the amount of things is WRONG")
        self.assertEqual(result, compare, "the list of things is WRONG")
        self.assertTrue(totalWeight <= 20, "the total weight violate constraint")
        self.assertEqual(totalValue, 255.0, "the total value of things is wrong")

class TestBruteKanpsack(unittest.TestCase):
    """  
    test all knapsack solver using brute force
    """
    def setUp(self) -> None:
        self.datas = {'clock' : [175, 10], 'painting' : [90, 9], 'radio' : [20, 4], 'vase' : [50, 2], 'book' : [10, 1], 'computer' : [200, 20]}
        # self.s = samples of things to be tested
        self.s = gk.buildThings(self.datas, cost_custom='weight')

    # start with the supprot
    def test_generate_binary_reps_digits(self):
        self.assertEqual(gk.getBinaryRep(0,4), '0000', "4 digits binary rep for 0 is WRONG")
        self.assertEqual(gk.getBinaryRep(2,6), '000010', "6 digits binary rep for 2 is WRONG")
        self.assertEqual(gk.getBinaryRep(15,8), '00001111', "8 digits binary rep for 15 is WRONG")

    def test_generate_binary_larger_than_digits_invoke_error(self):
        with self.assertRaises(ValueError) as cm:
            gk.getBinaryRep(8, 3)
        
        self.assertTrue("not enough digits" in cm.exception.args)

    def test_generate_binary_all_1s(self):
        self.assertEqual(gk.getBinaryRep(15,4), "1111", "4 digits binary reps for 15 is WRONG")
        

    def test_generating_powerset_from_simple_list(self):
        # preps
        self.powerset = gk.genPowerSet([1,2,3])
        self.assertEqual(self.powerset, [[],[3],[2],[2,3],[1],[1,3],[1,2],[1,2,3]])

    def test_optKnapsack_value(self):
        self.optVal, self.optList = gk.bruteKnapsack(self.s, 20, gk.Thing.getValue, gk.Thing.getCost)
        self.assertEqual(self.optVal, 275)
    
    def test_optKnapsack_opt_list(self):
        self.optVal, self.optList = gk.bruteKnapsack(self.s, 20, gk.Thing.getValue, gk.Thing.getCost)
        self.optResult = []
        for item in self.optList:
            self.subResult = []
            self.subResult.append(item.getName())
            self.subResult.append(item.getValue())
            self.subResult.append(item.getCost())
            self.optResult.append(self.subResult)
        
        self.assertEqual(self.optResult, [["clock", 175.0, 10.0], ["painting", 90.0, 9.0], ["book", 10.0, 1.0]])