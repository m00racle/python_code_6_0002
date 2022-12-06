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
    using greedy algoritm to solve knapsack problem
    given things : list = list of Thing type objects, constraint : int = max/min value of constraint
    keyFunction : function or lambda to determine comparables
    descending : boolean = True (default) the optimization to maximize
    returns list : optimum knapsack Thing type objects
    """
    result = []
    
    totalCost = 0

    thingsCopy = sorted(things, key=keyFunction, reverse=descending)
    
    for thing in thingsCopy:

        if (totalCost + thing.getCost()) <= constraint:
            result.append(thing)
            totalCost += thing.getCost()
            
    return result
