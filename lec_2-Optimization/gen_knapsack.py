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

