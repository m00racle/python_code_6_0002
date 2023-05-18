import random
from matplotlib import pyplot
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

def simFlip(numFlips:int)-> tuple:
    """  
    Given:
    numFlips : int = number of flips to be simulated
    return:
    tuple = (number of Heads:int, number of Tails: int)
    """ 
    numHeads = 0
    for n in range(numFlips):
        if random.random() < 0.5:
            numHeads += 1
    numTails = numFlips - numHeads
    return (numHeads, numTails)

def flipPlot(minExp:int, maxExp:int, numTrials:int)->None:
    """  
    Given:
    minExp: minimum 2**exp for the xAxis scale
    """
    xAxis, ratioMeans, ratioStdev, diffMeans, diffStdev = [], [], [], [], []
    for x in range(minExp , maxExp + 1):
        # preps the xAxis
        xAxis.append(2**x)

    for numFlip in xAxis:
        # simulate the flip
        ratios = []
        diffs = []
        for t in range(numTrials):
            numHeads, numTails = simFlip(numFlip)
            ratios.append(numHeads/float(numTails))
            diffs.append(abs(numHeads - numTails))
        ratioMeans.append(meanList(ratios))
        ratioStdev.append(stDev(ratios))
        diffMeans.append(meanList(diffs))
        diffStdev.append(stDev(diffs))

    # plot the position 0 diff mean
    plotTitle = f"Mean of Absolute difference #Heads - #Tails with {numTrials} trials"
    xTitle = "Number of Flips"
    yTitle = "Mean abs(#Head - #Tails)"
    pyplot.subplot(2,2,1)
    pyplot.title(plotTitle)
    pyplot.xlabel(xTitle)
    pyplot.ylabel(yTitle)
    pyplot.plot(xAxis, diffMeans, 'bo')
    pyplot.yscale('log')
    pyplot.xscale('log')

    # plot the position 1 diff stdev
    plotTitle = f"Standard Deviation difference #Heads - #Tails with {numTrials} trials"
    xTitle = "Number of Flips"
    yTitle = "Stdev abs(#Head - #Tails)"
    pyplot.subplot(2,2,2)
    pyplot.title(plotTitle)
    pyplot.xlabel(xTitle)
    pyplot.ylabel(yTitle)
    pyplot.plot(xAxis, diffStdev, 'bo')
    pyplot.yscale('log')
    pyplot.xscale('log')

    # plot the position 2 diff mean
    plotTitle = f"Mean of ratio (#Heads/#Tails) with {numTrials} trials"
    xTitle = "Number of Flips"
    yTitle = "Mean ratio (#Heads/#Tails)"
    pyplot.subplot(2,2,3)
    pyplot.title(plotTitle)
    pyplot.xlabel(xTitle)
    pyplot.ylabel(yTitle)
    pyplot.plot(xAxis, ratioMeans, 'bo')
    pyplot.yscale('log')
    pyplot.xscale('log')

    # plot the position 3 diff stdev
    plotTitle = f"Standard Deviation ratio (#Heads/#Tails) with {numTrials} trials"
    xTitle = "Number of Flips"
    yTitle = "Stdev ratio (#Heads/#Tails)"
    pyplot.subplot(2,2,4)
    pyplot.title(plotTitle)
    pyplot.xlabel(xTitle)
    pyplot.ylabel(yTitle)
    pyplot.plot(xAxis, ratioStdev, 'bo')
    pyplot.yscale('log')
    pyplot.xscale('log')


    # show the plots
    pyplot.show()


def main():
    random.seed(42)
    flipPlot(4,20,20)

if __name__ == '__main__':
    main()