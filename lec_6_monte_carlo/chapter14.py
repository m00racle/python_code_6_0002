"""  
    CHAPTER 14
    Monter Carlo Simulation
"""
import random

def rollDie():
    """  
    no Params given
    simulation or rolling die
    return : int random number between 1 to 6
    """
    return random.choice([1,2,3,4,5,6])

def checkPascal(numTrials):
    """  
    given:
        numTrials: int = number of trials simulating 24 die rolls 
        simulate the Pascal probability

        return: number = mean number of probability of winning 
        which is one of the 24 rolls output double six
    """
    numWins = 0
    for i in range(numTrials):
        for j in range(24):
            # toss double dice 24 times
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 == 6:
                numWins += 1
                # since we get the winning die we move to the next trial stage simulation
                break
    # return the probability of winning:
    return numWins/numTrials

def runPascal():
    prob = checkPascal(1000000)
    print(f"Probability of double dice wins: {prob}")

if __name__ == '__main__':
    random.seed(33)
    runPascal()