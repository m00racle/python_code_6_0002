# make the function to return the list of people with same date of birth ...
# this will be used to prove how many individual(s) in certain group ...
# having the same birthday.

import random

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

def test_run():
    """  
    running specific code to test
    """
    how = sameDate(10, 2)

if __name__ == '__main__':
    test_run()