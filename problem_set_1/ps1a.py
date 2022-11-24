###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:
import os
from ps1_partition import get_partitions
import time

dir = os.path.dirname(__file__)
#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # : Your code here
    cows = {}
    f = open(filename, "r")
    for x in f:
        st = x.split(",")
        cows[st[0]] = int(st[1])
    
    return cows

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    result = []
    # turn all the keys in cows dictionary into list.
    # sort the list from the most weight using the value from cows[key]
    cow_list = sorted(list(cows.keys()), key=lambda x : cows[x], reverse=True)

    # pop the cow from behind and append it to the list of trip
    weight = 0
    trip = []
    while len(cow_list) > 0:
        weight += cows[cow_list[-1]]
        if weight > limit:
            result.append(trip)
            trip = []
            weight = 0
            
        else:
            trip.append(cow_list.pop())
    
    # append the final trip to result:
    result.append(trip)
    # append the trip list into larger result list
    return result

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    pass
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    print("test")
    cows = load_cows(dir + "/ps1_cow_data.txt")
    print("using greedy transport:")
    greedy_result = greedy_cow_transport(cows)
    print(greedy_result)
    print(f'number of trips: {len(greedy_result)}')

if __name__ == '__main__':
    compare_cow_transport_algorithms()