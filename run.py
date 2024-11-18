import replit
from getkey import getkey, keys
import time

class Passenger:
    """A class to represent a passenger."""
    def __init__(self, age, gender, occupation):
        """Initialize passenger with age, gender, and occupation."""
        self.age = age
        self.gender = gender
        self.occupation = occupation 

class Bus:
    """
    Class to represent a bus.
    A bus holds a list of passengers and allows for adding, removing, 
    viewing passengers, and showing statistics.
    """
    def __init__(self):
        self.passengers = []