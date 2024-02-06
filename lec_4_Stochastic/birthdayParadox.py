# make the function to return the list of people with same date of birth ...
# this will be used to prove how many individual(s) in certain group ...
# having the same birthday.

import random
from math import factorial as fact

def sameDate(numPeople:int, numSame:int) -> bool:
    """  
    Given :
    numPeople:int = number of people in a group
    numSame:int = the prediction how many people having the same birthday

    See if the simulated number of people having the same birthday is above the predicted 
    number

    return : bool = whether max number of people with the same birthday > numSame
    """
    # declare (set) on your system how many days it is in a year:
    dates = range(366) 
    # NOTE: range 366 returns numbers from 0 to 365

    # uncomment following if you want to simulate deterministic prob on birthdays:
    # dates = 4*list(range(0, 57)) + [58]\
    #                + 4*list(range(59, 366))\
    #                + 4*list(range(180, 270))

    # make list consist of zeros as initial condition 
    birthdayPeople = [0] * 366
    # NOTE: use list since it is mutable so we can just change specific value in specific ..
    #       location, and also each zero will be incremented accoriding to position to ...
    #       simulate the number of people with specific date of birth.

    # iterate to all numPeople 
    for p in range(numPeople):
        birthday = random.choice(dates)
        # increment the index of the birthdayPeople to simulate there exist people at...
        # having that birth date.
        birthdayPeople[birthday] += 1

    return max(birthdayPeople) >= numSame

# but I want to make multiple trials at the same case
# then as parameter I will use the ratio where the simulation returns that there are 2 people...
# or more having the same birthday in a group to the how many trials is done

def simBirthday(numPeople:int, numSame:int, numTrials:int) -> float:
    """  
    Given:
    numPeople:int = the number of people in the simulate group
    numSame:int = the prediction of how many people in a group have the same birthday
    numTrials:int = how many simulation run for the same parameters

    return:float = ratio between how many times there are more than 2 people having the same...
    #               birthday to numTrials
    """
    # initialize number of correct (sameDate returns True)
    correct = 0

    # iterate for range of numTrials 
    for t in range(numTrials):
        # increment the correct if the sameDate returns True
        if sameDate(numPeople, numSame):
            correct += 1

    # divide the correct to numTrials and returns the output
    return correct/float(numTrials)


def test_run():
    """  
    running specific code to test
    """
    
    # now let's use them to simulate different number of people in a group:

    numDays = 366
    for numPeople in [10, 20, 40, 100]:
        print(f'for {numPeople}, estimated prob.of a shared birthdayis {simBirthday(numPeople,3,10000)}')
        
        # make comparison that using math formulation:
        numerator = fact(numDays)

        # NOTE: fact is math.factorial

        denom = (numDays**numPeople) * fact(numDays - numPeople)

        # print the math formulation 
        print(f'Actual (math) prob. for {numPeople} = {1 - numerator/denom}\n')
    

if __name__ == '__main__':
    test_run()