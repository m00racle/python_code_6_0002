"""  
This is more general nature of Knapsack
We start with more general implementation of Item class
"""

class Thing(object):
    """  
    more general form to describe Item in knapsack we call them thing now to differentiate to previous knapsack Item
    """
    def __init__(self, name : str, value : float, cost : float, value_name :str = 'value', cost_name : str = 'cost') -> None:
        self.name = name
        self.value = float(value)
        self.cost = float(cost)
        self.value_name = value_name
        self.cost_name = cost_name

    def __str__(self) -> str:
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

def buildThings(datas : dict, value_custom = 'value', cost_custom = 'cost') -> list:
    """  
    given datas : dict {name : [value, cost]} 
    returns list of Thing type
    """
    result = []
    for name in datas.keys():
        result.append(Thing(name, datas[name][0], datas[name][1], value_name=value_custom, cost_name=cost_custom))
    return result

def greedy(things: list, constraint : float, keyFunction, descending=True) -> list:
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
