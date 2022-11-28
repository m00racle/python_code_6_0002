"""  
Compare both fibs functions 
"""

def fibs(n: int, call = {'calls' : 0}):
    """  
    comventional fibonacci function
    given n : int a positive integer
    returns list (fibonacci at index n, number of recursive calls)
    """
    if n == 0 : return [0, call]
        # if memo['calls'] == 0 : return 0
        # else:
        #     memo['calls'] += 1
        #     return 0

    if n == 1 : return [1, call]
        # if memo['calls'] == 0 : return 1
        # else:
        #     memo['calls'] += 1
        #     return 1
    
    call['calls'] += 2
    return [fibs(n - 1, call)[0] + fibs(n - 2, call)[0], call]

def fastFibs(n: int, memo = {'calls': 0}):
    """  
    fast fibonacci function using memoization
    n : int = the index of the fibonacci number (starts with fastFibs(0) = 0)
    Returns list : [fibonacci number at index n, dictionary]
    """
    if n == 0 : return [0, memo]
    if n == 1 : return [1, memo]

    try:
        memo[n]
        text = 'access ' + str(n)
        memo[text] += 1
        return [memo[n], memo]
    except KeyError:
        text = 'access ' + str(n)
        memo[text] = 0
        memo['calls'] += 2
        result = fastFibs(n-1, memo)[0] + fastFibs(n-2, memo)[0]
        memo[n] = result
        return [result, memo]

def testRun():
    n = 10
    fibo, t = fibs(n)
    fastFibo, mem = fastFibs(n)
    # print(t['calls'])
    print(f"\nfibonnaci {n}th = {fibo}")
    print(f"using conventional run with {t['calls']} calls")

    print(f"\nfast fibonacci {n}th = {fastFibo}")
    print(f"using fast fibo function with {mem['calls']} calls")
    print (mem)

if __name__ == '__main__':
    testRun()
