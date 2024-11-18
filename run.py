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