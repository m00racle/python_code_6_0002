import random

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