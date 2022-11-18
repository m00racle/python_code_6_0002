class Item(object) :
    """  
    Class of Item
    init Params: name : str, value : float, weight : float

    """
    def __init__(self, name, value, weight) -> None:
        self.name = name
        self.value = float(value)
        self.weight = float(weight)
    
    # make getter function for the class
    def getName(self) -> str:
        return self.name
    def getValue(self) -> float:
        return self.value
    def getWeight(self) -> float:
        return self.weight
    
    # define print string representation (str rep) output __str__:
    def __str__(self) -> str:
        
        return '<' + self.name + ', ' + str(self.value) + ', ' + str(self.weight) + '>'

def value(item) -> float:
    """ 
    this is key function for sorter based on Item value 
    Params: item : Item
    Returns: float
    """
    return item.getValue()

def weightInverse(item) -> float:
    """  
    this is key function for sorter based on inverse weight (weight)
    Params: item : Item
    Returns: float
    """
    return 1.0/item.getWeight()

def density(item) -> float:
    """  
    this is key function for sorter on density (value / weight)
    Params: item : Item 
    Return: float
    """
    return item.getValue() / item.getWeight()

def buildItems():
    """  
    function to build a list of Item type objects
    Params : None
    Return : list of Item type objects
    """
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]

    # initiate empty list of Items
    Items = []
    # for loop iterate all items to be appended in Items
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items

def greedy(items, constraint, keyFunction):
    """  
    Given list of items sort it according to key function and take the available
    Parameters: items : list of objects type Item, constraint : the limit in this case weight, keyFunction : function for sort
    Returns: tuple of (list of Item type objects, total value: float)
    """
    totalValue = 0
    taken = []
    totalWeight = 0
    
    # make a copy of the items but sorted according to keyFunction:
    # remember we sorted decending from the biggest to the smallest 
    # this is why we use inverse weight instead of weight to represent weight as consideration
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    for item in itemsCopy:
        
        if (totalWeight + item.getWeight()) <= constraint:
            taken.append(item)
            totalWeight += item.getWeight()
            totalValue += item.getValue()

    return (taken, totalValue)

def printGreedy(items, constraint, keyFunction) -> None:
    """  
    Given items and constraint print the Greedy algorithm result based on KeyFunction
    Params: items : [Item], constraint : float, keyFunction : def (object)
    Return : None
    """
    # fetch the Greedy results
    (taken, totalValue) = greedy(items, constraint, keyFunction)
    print("Total Values of items taken: ", totalValue)
    for item in taken :
        print("   ", item)

def getBinaryRep(n : int, numDigits : int) -> str:
    """  
    Generate bunary representation of the sequence (NOT THE NUMBER)
    PARAMS: 
    n : int (The number you want to get representation)
    numDigits : int (the number of digits of the representation)
    """
    result = ''
    # get all the binary body
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    
    # ensure the binary rep does not longer than specified number of digits:
    if len(result) > numDigits:
        raise ValueError("not enough digits")
    # get the fillion of 0s for the rest of digits:
    for i in range(numDigits - len(result)):
        result = '0' + result
    
    return result

def genPowerSet(L : list) -> list:
    """  
        Generate power set
        Params: L (list of objects) : [objects] that will be processed 
        Returns : powerset : [[]] (list of list) 
    """
    powerset = []
    # define how many element the powerset will have:
    powerElement = 2**(len(L))
    
    # iterate to put subset into powerset according to binary rep rule:
    for i in range(0, powerElement):
        # get binary representation for i-th element of powerset
        binrep = getBinaryRep(i, len(L))
        # prepare subset to put the elements of the powerset
        subset = []

        for j in range(len(L)):
            # using binary rep rule if the bit is 1 it goes to subset if 0 then not
            if binrep[j] == '1':
                subset.append(L[j])
        # append the subset into powerset
        powerset.append(subset)
        
    return powerset

def optKnapsack01(pset : list, maxWeight : int, getVal, getWeight) -> tuple :
    """  
    Given:
    pset : powerset list of list all combinations of Items
    maxWeight : maximum wight the knapsack can carry
    getVal : lambda function to getValue (float) of the item (using lambda function)
    getWeight: lambda function to getWeight (float) of the item

    Return: tuple
    optVal : optimum Value of all items taken
    optList : optimum list of items taken
    """
    optVal = 0
    optList = []
    # begin with iterate the list of items in pset
    for items in pset:
        currentWeight = 0
        currentValue = 0
        for item in items:
            currentWeight += getWeight(item)
            currentValue += getVal(item)
        if currentWeight <= maxWeight:
            if currentValue > optVal:
                optList = items
                optVal = currentValue


    return (optVal, optList)

    
def runGreedy(maxWeight=20):
    # preps list of all items
    items = buildItems()

    print("Use Greedy by Value to fill knapsack in size", maxWeight)
    printGreedy(items, maxWeight, value)

    print("Use Greedy by weight to fill knapsack in size", maxWeight)
    printGreedy(items, maxWeight, weightInverse)

    print("Use Greedy by Density to fill knapsack in size", maxWeight)
    printGreedy(items, maxWeight, density)



if __name__ == '__main__':
    runGreedy()

