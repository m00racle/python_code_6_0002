###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    # base case
    if len(egg_weights) == 0 or target_weight <= 0:
        return 0
    # recursive case
    if (target_weight - egg_weights[-1]) < 0:
        # pop the last (largest) egg weights (dynamic to simpler egg weights)
        amount = dp_make_weight(egg_weights[:-1], target_weight)
        # no amount increment when this if case happen to be TRUE
    else:
        # diminish the target wieght with the largest egg weight
        amount = dp_make_weight(egg_weights, (target_weight - egg_weights[-1]))
        # if this case happen then the amount of egg is added by one
        amount += 1
    return amount

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
    print("next experiment: (1, 3, 7, 13)")
    print("target: 131")
    print(f'result: {dp_make_weight((1, 3, 7, 13), 131)}')