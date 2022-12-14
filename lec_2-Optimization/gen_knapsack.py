"""  
This is more general nature of Knapsack
We start with more general implementation of Item class
"""

class Thing(object):
    """  
    more general form to describe Item in knapsack we call them thing now to differentiate to previous knapsack Item
    """
    def __init__(self, name : str, value : float, cost : float, *, 
    value_name : str = 'value',
    cost_name : str= 'cost',
    **kwargs) -> None:
        """  
        initialize class Thing:
        parameters:
        name : str = name of the item
        value : float = the value of the item (definintion of value is customizable)
        cost : float = the cost of the item (definition of cost is customizable)

        kwargs: ( => means override/ if this name on kwargs then it will override the named variable )
        value_custom_name : str => value_name (default = 'value') = the definition of value variable of the Thing
        cost_custom_name : str => cost_name (default = 'cost') = the definition of the cost variable of the thing
        """
        refs = {
            'value_custom_name' : value_name,
            'cost_custom_name' : cost_name
        }

        for r in kwargs:
            if r in refs:
                refs[r] = kwargs[r]

        
        self.name = name
        self.value = float(value)
        self.cost = float(cost)
        self.value_name = refs['value_custom_name']
        self.cost_name = refs['cost_custom_name']

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

def buildThings(data : dict, *, 
    value_custom : str = 'value',
    cost_custom : str = 'cost',
    **kwargs) -> list:
    """  
    Description: helper function to make list of Item type objects

    Parameter:
    data : dict {name : [value, cost]} = dictionary with Item's name as key and list of value, cost as value

    kwargs: ( => means override/ if this name on kwargs then it will override the named variable )
    value_custom_name : str => value_custom (default = 'value') = the definition of value variable of the Thing
    cost_custom_name : str => cost_custom (default = 'cost')

    Return:
    list of Thing type objects

    """
    addon = {
        'value_custom_name' : value_custom,
        'cost_custom_name' : cost_custom
    }

    for k in kwargs:
        if k in addon :
            addon[k] = kwargs[k]
        else:
            continue

    
    result = []
    # this is kwargs for the Thing init function:
    customs = {
        'value_custom_name' : addon['value_custom_name'], 
        'cost_custom_name' : addon['cost_custom_name']
    }
    for name in data.keys():
        result.append(Thing(name, data[name][0], data[name][1], **customs))
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

def recursiveKnapsack(consider: list, avail: float, taken: tuple = (), val: float = 0, **recSet) -> list:
    """  
    Description: function to optimize knapsack case using recursive programming

    Parameter:
    consider : list = list of Thing type objects to be optimized
    avail : float = the constraint of knapsack available capacity
    taken : tuple = list of Thing type objects taken durin optimization (default = ())
    NOTE: I use tuple since it is immutable, if I use list then it will reference the same list 
          which will return to None or [] each recursive calls!!
    val : float = value of all taken objects (default = 0)
    memo: Here memo is only used to record number of recursive calls to recursiveKnapsack function until; it founds the opt

    NOTE: when taking things into knapsack basically the algorithm added something backward thus if item b is considered before item c then item c will be added prior to item b

    return : list = [[consideration left over], available_left: float, (optimized Thing), optimized_value: float]
    """
    k = {'go': False, 'recMemo' : {'calls': 0}}
    for i in recSet:
        if i in k:
            k[i] = recSet[i]
    
    if k['go'] == False : k['recMemo'] = {'calls': 0}
    memo = k['recMemo']

    if consider == [] or avail == 0 :
        if len(taken) > 0 : return [consider, avail, taken, val, memo]
        # add nothing since there are nothing to be added anymore
        return [consider, avail, (), 0, memo]
    elif avail  < consider[0].getCost() :
        # insufficient available capacity to stored the next thing in the scenario
        # WRONG: set value to be 0 because this should not even considered
        # CORRECT: only consider the right side only, val is not changing since not included consider[0]
        return recursiveKnapsack(consider[1:], avail, taken, val, recMemo=memo, go=True)
    else :
        consThing = consider[0]
        nextAvail = avail - consThing.getCost()
        if not('calls' in memo): memo['calls'] = 0
        memo['calls'] += 1
        cons_1, avail_1, taken_1, val_1, memo = recursiveKnapsack(consider[1:], nextAvail, taken, val, recMemo=memo, go=True)
        # this is basically reverse added the thing thus the value which thing is added is get added with consThing here
        # remember things are added here not included during the recursive calls
        val_1 += consThing.getValue()

        memo['calls'] += 1
        cons_2, avail_2, taken_2, val_2, memo = recursiveKnapsack(consider[1:], avail, taken, val, recMemo=memo, go=True)

        if val_2 < val_1 : return [cons_1, avail_1, (*taken_1, consThing), val_1, memo]
        else : return [cons_2, avail_2, taken_2, val_2, memo]

def dynamicKnapsack(consider: list, avail: list, taken: tuple = (), val: float = 0, **dynSet)-> list:
    """  
    Description: function to optimize knapsack case using recursive programming

    Parameter:
    consider : list = list of Thing type objects to be optimized
    avail : float = the constraint of knapsack available capacity
    taken : tuple = list of Thing type objects taken durin optimization (default = ())
    NOTE: I use tuple since it is immutable, if I use list then it will reference the same list 
          which will return to None or [] each recursive calls!!
    val : float = value of all taken objects (default = 0)
    memo: Here memo is only used to record number of recursive calls to recursiveKnapsack function until; it founds the opt

    NOTE: when taking things into knapsack basically the algorithm added something backward thus if item b is considered before item c then item c will be added prior to item b

    return : list = [[consideration left over], available_left: float, (optimized Thing), optimized_value: float]
    """
    j = {'go': False, 'dynMemo' : {'pull': 0, 'calls': 0}}
    for i in dynSet:
        if i in j:
            j[i] = dynSet[i]
    
    if not(j['go']): j['dynMemo'] = {'pull': 0, 'calls': 0}
    memo = j['dynMemo']

    # here is the difference from the recursive one:
    if (len(consider), avail) in memo : 
        if not('pull' in memo): memo['pull'] = 0
        memo['pull'] += 1
        return memo[len(consider), avail]
        
    if consider == [] or avail == 0 :
        if len(taken) > 0 : return [consider, avail, taken, val, memo]
        # add nothing since there are nothing to be added anymore
        return [consider, avail, (), 0, memo]
    elif avail  < consider[0].getCost() :
        # insufficient available capacity to stored the next thing in the scenario
        # WRONG: set value to be 0 because this should not even considered
        # CORECT: only consider the right side:
        return dynamicKnapsack(consider[1:], avail, taken, val, dynMemo = memo, go=True)
    else :
        consThing = consider[0]
        nextAvail = avail - consThing.getCost()
        if not('pull' in memo): memo['pull'] = 0
        # NOTE: I put pull here to ensure that when memoization turns out to be not useful (in some cases they do) The debugger
        # still able to take a look at the pull key data in the memo which should return value = 0
        if not('calls' in memo): memo['calls'] = 0
        memo['calls'] += 1
        cons_1, avail_1, taken_1, val_1, memo = dynamicKnapsack(consider[1:], nextAvail, taken, val, dynMemo = memo, go=True)
        # this is reverse taking things so added things add Value after recursive calls here 
        # remember things are added here not included during the recursive calls
        val_1 += consThing.getValue()

        memo['calls'] += 1
        cons_2, avail_2, taken_2, val_2, memo = dynamicKnapsack(consider[1:], avail, taken, val, dynMemo = memo, go=True)

        if val_2 < val_1 : 
            # here is when we took the memo
            result = [cons_1, avail_1, (*taken_1, consThing), val_1, memo]
            memo[(len(consider), avail)] = result
            
        else : 
            # here also the same thing happen
            result = [cons_2, avail_2, taken_2, val_2, memo]
            memo[len(consider), avail] = result
            
        return result