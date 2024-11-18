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
    
     def run(self):
        """
        Function to run the bus system.
        Presents a menu for adding, removing, and viewing passengers, as well as showing statistics.
        """
        while True:
            replit.clear()
            choice = get_choice_with_arrows(["Add passenger", "Remove passenger", "Show passenger list", "Statistics", "Exit"])

            if choice == "Add passenger":
                self.add_passenger()
            elif choice == "Remove passenger":
                self.remove_passenger()
            elif choice == "Show passenger list":
                self.view_passengers()
            elif choice == "Statistics":
                self.show_statistics()
            elif choice == "Exit":
                break