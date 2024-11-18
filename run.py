import replit
from getkey import getkey, keys
import time

def get_choice_with_arrows(options):
    """
    Function to get the user's choice with arrows using getkey.
    Displays menu options with an arrow for the selected option.
    """
    cursor = 0

    while True:
        replit.clear()

        for i, option in enumerate(options, start=1):
            arrow = "<" if i - 1 == cursor else " "
            print(f"{i}. {option:<24} {arrow}")

        keypressed = getkey()
        if keypressed == keys.DOWN and cursor + 1 != len(options):
            cursor += 1
        elif keypressed == keys.UP and not (cursor == 0):
            cursor -= 1
        elif keypressed == keys.ENTER:
            return options[cursor]

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

        def add_passenger(self):
            """
            Function to add a passenger to the bus.
            Asks the user for the passenger's age, gender, and occupation and adds them to the passenger list.
            """
            while True:
                replit.clear()
                age = get_age()
                gender = get_gender()
                occupation = get_occupation()
                replit.clear() 
                passenger = Passenger(age, gender, occupation)
                self.passengers.append(passenger)
                print("Passenger added successfully...")
                time.sleep(1)

                additional_choice = get_choice_with_arrows(["Return to menu", "Add a new passenger"])

                if additional_choice == "Return to menu":
                    break