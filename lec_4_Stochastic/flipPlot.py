import random
from matplotlib import pyplot

def flipPlot(minExp, maxExp):
    """  
    Params:
    minExp: int = exponent of 2 of minimum number of flips
    maxExp: int = exponent of 2 of maximum number of flips
    maxExp > minExp
    
    Plot: results of 2**minExp to 2**maxExp of coin flips
    """
    ratios = []
    diffs = []
    xAxis = []

    for exp in range(minExp, maxExp + 1):
        # this will inclued maxExp
        xAxis.append(2**exp)
    
    # now using each number in xAxis as number of flips
    for numFlips in xAxis:
        numHead = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHead += 1
        numTail = numFlips - numHead
        # add ratio between numHead/numTail:
        ratios.append(numHead/float(numTail))
        # add diff between |numHead - numTail|
        diffs.append(abs(numHead - numTail))
    
    # plotting the diffs
    pyplot.subplot(1,2,1)
    pyplot.title("Difference Between Heads and Tails")
    pyplot.xlabel("Number of flips")
    pyplot.ylabel("abs(#Head - #Tail)")
    pyplot.plot(xAxis, diffs, 'bo')
    pyplot.yscale('log')
    pyplot.xscale('log')
    # pyplot.show()

    # plotting the ratios
    pyplot.subplot(1,2,2)
    pyplot.title("Head/Tail ratios")
    pyplot.xlabel("Number of flips")
    pyplot.ylabel("#Heads/#Tails")
    pyplot.plot(xAxis, ratios, 'r+')
    # pyplot.yscale('log')
    pyplot.xscale('log')
    
    # show all plots 
    pyplot.show()


def main():
    print(f'Running function\n')
    random.seed(0)
    flipPlot(4, 20)

if __name__ == '__main__':
    main()