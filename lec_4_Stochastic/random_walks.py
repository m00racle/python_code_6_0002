"""  
Intro to Computation and Programming
Chapter 13 (Chapter 14 in 2nd ed text book)
Random Walks and More About Data Visualization
"""

from math import sqrt
import random

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
    