"""  
This is more general nature of Knapsack
We start with more general implementation of Item class
"""

class Thing(object):
    """  
    more general form to describe Item in knapsack we call them thing now to differentiate to previous knapsack Item
    """
    def __init__(self, name : str, value : float, cost : float, **kwargs) -> None:
        """  
        initialize class Thing:
        parameters:
        name : str = name of the item
        value : float = the value of the item (definintion of value is customizable)
        cost : float = the cost of the item (definition of cost is customizable)

        kwargs:
        value_name : str = the definition of value variable of the Thing (default = 'value')
        cost_name : str = the definition of the cost variable of the thing (default = 'cost')
        """
        refs = {
            'value_name' : 'value',
            'cost_name' : 'cost'
        }

        for r in kwargs:
            if r in refs:
                refs[r] = kwargs[r]

        
        self.name = name
        self.value = float(value)
        self.cost = float(cost)
        self.value_name = refs['value_name']
        self.cost_name = refs['cost_name']

    def __str__(self) -> str:
        """  
        Description: string representation of the class
        this function is called whenever print(Item.type.instance) is executed

        return:
        string : print output as class Representation
        """
        text = '<' + self.name + '; ' + self.value_name + ': ' + str(self.value) + '; ' + self.cost_name + ': ' + str(self.cost) + '>'
        return text 

    def getName(self) -> str:
        return self.name

    def getValue(self) -> float:
        return self.value

    def getCost(self) -> float:
        return self.cost

    def getValueName(self) -> str:
        return self.value_name

    def getCostName(self) -> str:
        return self.cost_name

def buildThings(datas : dict, **kwargs) -> list:
    """  
    Description: helper function to make list of Item type objects

    Parameter:
    datas : dict {name : [value, cost]} = dictionary with Item's name as key and list of value, cost as value

    Return:
    list of Thing type objects

    kwargs:
    value_custom : str = the name of the value variable name (default = value)
    cost_custom : str = the name of the cost variable (default = cost)
    ***************************************************************************
    """
    addon = {
        'value_custom' : 'value',
        'cost_custom' : 'cost'
    }

    for custom in kwargs:
        if custom in addon:
            addon[custom] = kwargs[custom]
    
    result = []
    for name in datas.keys():
        result.append(Thing(name, datas[name][0], datas[name][1], value_name=addon['value_custom'], cost_name=addon['cost_custom']))
    return result

def greedy( 
    things: list, #list of Item type objects
    constraint : float, # constraint of the cost
    keyFunction, # function to be used to sorted the Item list
    descending=True #if True sorted descending False otherwise
) -> list:
    """  
    Description: using greedy algoritm to solve knapsack problem

    Parameters:
    things : list = list of Thing type objects, constraint : int = max/min value of constraint
    keyFunction : function or lambda to determine comparables
    descending : boolean = True (default) the optimization to maximize

    returns: list = optimum list of knapsack Thing type objects
    """
    result = []
    
    totalCost = 0

    thingsCopy = sorted(things, key=keyFunction, reverse=descending)
    
    for thing in thingsCopy:

        if (totalCost + thing.getCost()) <= constraint:
            result.append(thing)
            totalCost += thing.getCost()
            
    return result

# start the brute force functions
# begin with building function to return binary reps of decimal numbers

def getBinaryRep(dec : int, numDigits : int) -> str:
    """  
    Description: function to return binary representation of a decimal number within certain number of binary digits

    Parameters:
    dec : int = the interger which required to be transformed into binary rep.
    numDigits : int = number of digits will be used to represent the integer dec

    return: str = string representation of binary rep for dec : int
    throw: ValueError if the number of digits is insufficient to represent the dec : int
    
    """
    reps = ''
    while dec > 0:
        reps = str(dec % 2) + reps
        dec = dec // 2
    
    # test if numDigits is sufficient:
    if len(reps) > numDigits : raise ValueError('not enough digits')

    for i in range(numDigits - len(reps)):
        reps = str(0) + reps

    return reps

def genPowerSet(inputSet : list) -> list:
    """  
    Description: function to create Power set from a set

    Parameter:
    inputSet : list = list of objects that represent a set

    Returns : list of list = list of all subsets of the original set a.k.a power set
    """
    powerSet = []
    for i in range(2**(len(inputSet))):
        subset = []
        binaries = getBinaryRep(i, len(inputSet))

        for k in range(len(binaries)):
            if binaries[k] == '1' : subset.append(inputSet[k])
        
        powerSet.append(subset)
    
    return powerSet

def bruteKnapsack(inputs: list, constraint : float, valueFunction, costFunction) -> tuple:
    """  
    Description: function for knapsack optimization with Brute Force Algorithm

    Parameter:
    inputs: list = list of Things type objects
    constraint : float = constraint limit of cost
    valueFunction : function = function returns value of Thing type
    costFunction : function = function returns cost of a Thing type

    Return: tuple = (float: total value of Things in list, list of Thing type objects)
    """
    # generate power set of all things in inputs set:
    powerSet = genPowerSet(inputs)
    # iteration for all set in powerset
    opt_list = []
    max_value = 0
    for set in powerSet:
        total_value = 0
        total_cost = 0
        output_list = []

        # iteration inside each subset:
        for item in set:
            if total_cost + costFunction(item) <= constraint:
                output_list.append(item)
                total_value = total_value + valueFunction(item)
                total_cost = total_cost + costFunction(item)
            else: 
                break
        if total_value > max_value:
            max_value = total_value
            opt_list = output_list
    
    return (max_value, opt_list)

def dynamicKnapsack(consider: list, avail: float, taken: tuple = (), val: float = 0) -> list:
    """  
    Descrioption: function to optimize knapsack case using dynamic programming

    Parameter:
    consider : list = list of Thing type objects to be optimized
    avail : float = the constraint of knapsack available capacity
    taken : list = list of Thing type objects taken durin optimization (default = [])
    val : float = value of all taken objects (default = 0)
    """
    if taken == None : taken = []
    if consider == [] :
        return [consider, avail, taken, val]
    elif avail < 0 :
        # set value to be 0 because this should not even considered
        return [consider, avail, taken, 0]
    else :
        consThing = consider[0]
        nextAvail = avail - consThing.getCost()
        nextTaken = (*taken, consThing)
        nextVal = val + consThing.getValue()
        cons_1, avail_1, taken_1, val_1 = dynamicKnapsack(consider[1:], nextAvail, nextTaken, nextVal)
        
        cons_2, avail_2, taken_2, val_2 = dynamicKnapsack(consider[1:], avail, taken, val)

        if val_2 < val_1 : return [cons_1, avail_1, taken_1, val_1]
        else : return [cons_2, avail_2, taken_2, val_2]