"""  
Intro to Computation and Programming
Chapter 13 (Chapter 14 in 2nd ed text book)
Random Walks and More About Data Visualization
"""

from math import sqrt
import random
from chapter12 import meanList, CV

class Location(object):
    """  
    object describing the location of the Drunkard in the field
    Field will be simulated as look alike a Cartesian Diagram
    the steps taken by the drunkard will follow only 4 (North, South, East, West)
    that will be simulated in this location
    """

    def __init__(self, x:float, y:float) -> None:
        """  
        initialize location 
        Params:
        x : float = x coordinate of the location
        y : float = y coordinate of the location
        """
        self.x = float(x)
        self.y = float(y)

    def move(self, deltaX:float, deltaY:float):
        """  
        simulate movement

        deltaX : float = the range of the movement along x axis
        deltaY : float = the range of the movement along y axis

        return : Location = new Location object updated to the movement
        """
        return Location(self.x + float(deltaX), self.y + float(deltaY))
    
    def getX(self) -> float:
        """  
        getter for x coordinate
        """
        return self.x
    
    def getY(self) -> float:
        """  
        getter for y coordinate
        """
        return self.y
    
    def distFrom(self, other):
        """  
        Calculate the range between two location (current self and other)
        Params:
        other : Location = other Location object that being used as base of the measurement

        Return: float = the distance from the start (other) to current (self) Location
        """
        xDist = self.x - other.x 
        yDist = self.y - other.y 
        return sqrt(xDist**2 + yDist**2)
    
    def __str__(self) -> str:
        """ 
        string representation for print and str
        """
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
    
class Drunk(object):
    """  
    Class represent Drunk object (Abstract)
    You need sub class to implement more methods related to specific Drunk
    the sub class MUST have takeStep method with clear definition!
    """
    def __init__(self, name:str=None) -> None:
        """  
        name : String = name of the Drunkard (default = None)
        """
        self.name = name

    def __str__(self) -> str:
        """  
        String representation for the class instance for print or str
        """
        if self.name != None:
            return self.name
        return 'Anonymous'
    
class UsualDrunk(Drunk):
    """  
    sub-class (implementation) of the Super Class Drunk
    Represent Usual Drunkard
    """
    def takeStep(self):
        """  
        Given list of possible steps taken by the drunkard
        Randomly selected one choice

        Return : tuple = pair of delta X and delta Y pair for movement
        """
        stepChoices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class Field(object):
    """  
    Represent the field where the drunkard will randomly walk
    it should be able to accomodate multiple drunkards if needed
    """
    def __init__(self) -> None:
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        """  
        Add another (must be unique) drunkard into the field
        Params:
        drunk : Drunk = Drunk type object represent one drunkard
        loc : Location = initial location of the Drunkard as put in the field

        Return: None
        """
        if drunk in self.drunks:
            # NOTE: I still don't have clue how to compare equality for this
            raise ValueError('Duplicate Drunk')
        else:
            self.drunks[drunk] = loc
    
    def moveDrunk(self, drunk):
        """  
        Move one Drunk (specified) 
        Params:
            drunk : Drunk = selected drunk to move (must present in the field)
        
        Return: None
        """
        if drunk not in self.drunks:
            raise ValueError('Drunk not in the field')
        xDist, yDist = drunk.takeStep()
        # open the location data of the drunkard
        currentLoc = self.drunks[drunk]
        # modify the location with the xDist and yDist form the drunkard movement:
        self.drunks[drunk] = currentLoc.move(xDist, yDist)

    def getLoc(self, drunk):
        """  
        get the location of a (specific) drunkard
        IF the drunkard is still and or available on the field

        Params:
        drunk : Drunk = specific drunkard object

        Return : Location = location of the specific drunkard
        """
        # make sure the drunk is on the field
        if drunk not in self.drunks:
            raise ValueError('Drunk not in the field')
        return self.drunks[drunk]
    
def walk(f:Field, d:Drunk, numSteps:int) -> float:
    """  
    Calculate the walk distance 
    Params:
        f : Field = Field object where the walk happens
        d : Drunk = Drunkard specific which on the field walking
        numSteps : int = Number of steps executed by the Drunkards

    Return : float = the difference final location and its start of the walk
    """
    # find where the drunkard starts
    start = f.getLoc(d)
    # move the drunkard number of steps
    for s in range(numSteps):
        f.moveDrunk(d)
    # calculate the distance to the last drunkard location from the start
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps:int, numTrials:int, dClass: Drunk) -> list:
    """  
    Simulate multiple random walk of a drunkard
    Params:
        numSteps : int = number of steps for each simulation session
        numTrials : int = number of simulation trials
        dClass : Drunk = implementation of sub class instance of a Drunk class
    
    Return : List = list of distances of all simulation trials
    """
    Homer = dClass()
    origin = Location(0.0, 0.0)
    distances = []
    # start trials
    for t in range(numTrials):
        # make field
        f = Field()
        f.addDrunk(Homer, origin)
        # put the session result in distances
        distances.append(walk(f, Homer, numSteps))
    
    return distances

def drunkTest(walkLengths:tuple, numTrials:int, dClass:Drunk) -> None:
    """  
    Testing Random walk mean distances and Coeff of Variance
    Params:
        walkLengths : tuple = sequence of ints (positive) of each represent numSteps
        numTrials : int = number of trials in simulation
        dClass : Drunk = implementation or sub class of Drunk class
    Return: None
    """
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(f"\n{dClass.__name__} random walk of {numSteps} steps")
        print(f"Mean = {meanList(distances)}")
        print(f"CV = {CV(distances)}")
        print(f"Maximum distance = {max(distances)}")
        print(f"Minimum distances = {min(distances)}")


# run point
if __name__ == '__main__':
    # run drunk test
    drunkTest((10, 100, 1000), 100, UsualDrunk)
    drunkTest((0,1), 100, UsualDrunk)