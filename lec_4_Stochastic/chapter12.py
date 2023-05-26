import random
from math import sqrt

def meanList(x:list) -> float:
    """  
    Given:
    x : List of numbers
    Return: float mean of all numbers in the list
    """
    return float(sum(x))/len(x)

def stDev(x:list) -> float:
    """  
    Given x: List of numbers
    Return : float standard deviation of all numbers in the list
    """
    mean = meanList(x)
    tot = 0.0 
    for i in x:
        tot += (i - mean)**2
    # return square root of total / len(x)
    return sqrt(tot/len(x))

def CV(x:list) -> float:
    """  
    Given:
    x : list = list of number

    Return:
    float = Coeff of Variance for all numbers in list x
    """
    try:
        return stDev(x)/meanList(x)
    except ZeroDivisionError:
        return float('nan')


def rollDie()->int:
    """  
    returns random number int between 1 to 6
    """
    return random.choice([1,2,3,4,5,6])

def rollN(n)->str:
    """  
    Given n: int = number of roll die
    Returns : str = sequence of die roll results
    """
    result = ''
    for i in range(n):
        result += str(rollDie())
    print(f"die rolls result sequence: {result}")

def run():
    """  
    run the page
    """
    # rollDie for 10 times and print the output sequence
    print("Test roll die 10 times:")
    rollN(10)


if __name__ == '__main__':
    run()