import matplotlib.pyplot as plt
from coinHIst import simFlips
import random
from numpy import array as ar

def showErrorBars(minExp:int, maxExp:int, numTrials:int) -> None:
    """  
    Make ErrorBars from coin flips experiment
    Given:
    minExp:int = exponent for minimum number of coin flips per trials
    maxExp:int = exponent for maximum number of coin flips per trials
    numTrials:int = number of trials of the same time coin is flipped

    Returns: None
    """
    # WE only need mean and stdev 
    avgs, sds = [], []
    xAxis = []
    for expo in range(minExp, maxExp + 1):
        xAxis.append(2**expo)
        # find the mean and stdev for each xAxis
        fracs, mean, stdev = simFlips(2**expo, numTrials)
        avgs.append(mean)
        sds.append(stdev)
    
    # prepare the plot which using pyplot
    plt.errorbar(xAxis, avgs, yerr= 2 * ar(sds))
    # NOTE:
    """  
    The ar is numpy array. why do I need to put this here?
    Because I want to multply each element of the sds list by 2 but I can't do this directly
    Since sds is a list, I need to convert sds into a scalar (which is not what I want)
    Or I can make it like a 1 x n matrix which is an array
    """

    # set the xAxis to have semilog scale
    plt.semilogx()

    # show the plot
    plt.show()

def main():
    # set the random seed for consistency: 42
    random.seed(42)
    showErrorBars(3,10,100)

if __name__ == '__main__':
    main()