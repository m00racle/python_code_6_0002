import random
from chapter12 import meanList, stDev
from matplotlib import pyplot as plt

def flip(numFlips:int) -> float:
    """  
    simulate 1 trial of coin flip 
    given: 
    numFlip: int = how many flip to be simulated

    return:
    float = ratio between heads/tails
    """
    heads = 0.0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1
    return heads/numFlips

def simFlips(numFlipsPerTrial:int, numTrials:int) -> tuple:
    """  
    simulate coin flip for number of trials
    Given:
    numFlipsPerTrial:int = number of coin flips per trial
    numTrials:int = number of trials 

    Return: tuple
    fracHeads: list = [number of frac heads/flips in one trial]
    mean: float = mean of all frac heads/flips
    sd: float = standard deviation of the mean
    """
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    return(fracHeads, meanList(fracHeads), stDev(fracHeads))

def compareHistPlot(numFlips1:int, numFlips2:int, numTrials:int) -> None:
    """  
    Compare two flip simulation histogram chart
    Given:
    numFlips1:int = number of flips/trial of simulation 1
    numFlips2:int = number of flips/trial of simulation 2
    numTrials:int = number of trials

    Return: None
    """
    data1, mean1, sd1 = simFlips(numFlips1, numTrials)
    data2, mean2, sd2 = simFlips(numFlips2, numTrials)
    # plot
    xTitle = "Fraction of Heads"
    yTitle = "Number of Trials"
    # text_kwargs = dict(ha='center', va='center', fontsize=18, color='red')
    # simulation 1
    plotTitle1 = f"{numTrials} trials of {numFlips1} filps each"
    plt.subplot(2,1,1)
    plt.title(plotTitle1)
    plt.xlabel(xTitle)
    plt.ylabel(yTitle)
    plt.hist(data1, bins=20)
    
    # extract the xlim
    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()
    plt.text(xmin, (ymax-ymin)/2, f' mean: {mean1:.4f}\n stdev: {sd1:.4f}', color='red')

    # simulation 2
    plotTitle2 = f"{numTrials} trials of {numFlips2} filps each"
    plt.subplot(2,1,2)
    plt.title(plotTitle2)
    plt.xlabel(xTitle)
    plt.ylabel(yTitle)
    plt.hist(data2, bins=20)
    # set the x limits to be the hist 1 so it can be compared
    plt.xlim(xmin, xmax)
    # extract the ylim
    ymin, ymax = plt.ylim()
    plt.text(xmin, (ymax-ymin)/2, f' mean: {mean2:.4f}\n stdev: {sd2:.4f}', color='red')

    # show the plot
    plt.show()

def main():
    random.seed(42)
    compareHistPlot(100,1000,100000)

if __name__ == '__main__':
    main()