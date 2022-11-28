"""  
Compare both fibs functions 
"""

def fibs(n: int, memo = {'calls' : 0}):
    """  
    comventional fibonacci function
    given n : int a positive integer
    returns tuple (fibonacci at index n, number of recursive calls)
    """
    if n == 0 : return [0, memo]
        # if memo['calls'] == 0 : return 0
        # else:
        #     memo['calls'] += 1
        #     return 0

    if n == 1 : return [1, memo]
        # if memo['calls'] == 0 : return 1
        # else:
        #     memo['calls'] += 1
        #     return 1
    
    memo['calls'] += 2
    return [fibs(n - 1, memo)[0] + fibs(n - 2, memo)[0], memo]
