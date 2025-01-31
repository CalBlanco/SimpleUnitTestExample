import math

DISTANCE_LIMIT = 30

class NamedCoords:
    """Some random class that has a couple of methods and fields"""

    def __init__(self, x:int, y:int, word:str):
        self.x = x
        self.y = y
        self.word = word
    
    def __eq__(self, other):
        """Returns true given both have the same coords (ignores word)"""
        return (self.x == other.x and self.y == other.y)

    def __repr__(self):
        return f'Named-Coords: ({self.x}, {self.y}) - {self.word}'

    def __str__(self): #just return the representation
        return self.__repr__()


    def __add__(self, other): 
        """add coords together"""
        return (self.x + other.x, self.y + other.y)
    

    def __sub__(self, other): #create a tuple 
        return (self.x - other.x, self.y - other.y)
    
    def calc_distance(self, point):
        """Calculate a distance, throw an exception if the distance is over some arbitrary limit, or if point tuple 
        is missing values
        """
        x, y = self - point #call our sub method
        dist = math.sqrt( (x ** 2) + (y ** 2))
        if dist > DISTANCE_LIMIT:
            raise Exception('Over arbitrary limit')
        return dist
    

