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

def get_age():
    """
    Function to get validated age input from the user.
    Asks the user to input an age between 1 and 200.
    """
    replit.clear()
    while True:
        try:
            age = int(input("Enter your age (1-200): "))
            if 1 <= age <= 200:
                return age
            else:
                print("\nSomething went wrong! Enter a valid age between 1 and 200.\n")
        except ValueError:
            print("\nSomething went wrong! Enter a valid age as a number.\n")

def get_gender():
    """
    Function to get validated gender input from the user.
    Allows selection between 'man', 'woman', and 'non-binary'.
    """
    while True: 
        replit.clear()
        gender_options = ["man", "woman", "non-binary"]
        return get_choice_with_arrows(gender_options)

def get_occupation():
    """
    Function to get validated occupation input from the user.
    Allows selection between different occupations such as 'employed', 'unemployed', etc.
    """
    while True:
        replit.clear()
        occupation_options = [
            "employed",
            "unemployed",
            "student",
            "teenager under 18",
            "housewife",
            "child under 7 years"
        ]
        replit.clear()
        return get_choice_with_arrows(occupation_options)

def calculate_age_statistics(passengers): 
    """
    Function to calculate age statistics for the passengers.
    Returns average age, youngest age, and oldest age.
    """
    if not passengers:
        return None

    ages = [passenger.age for passenger in passengers]
    average_age = sum(ages) / len(passengers)
    min_age = min(ages)
    max_age = max(ages)

    return average_age, min_age, max_age

def calculate_gender_percentage(passengers):
    """
    Function to calculate the percentage of passengers by gender.
    Returns a dictionary with the gender percentages.
    """
    if not passengers:
        return None

    gender_count = {"man": 0, "woman": 0, "non-binary": 0}

    for passenger in passengers:
        gender_count[passenger.gender] += 1

    total_passengers = len(passengers)
    percentage = {gender: (count / total_passengers) * 100 for gender, count in gender_count.items()}

    return percentage

def calculate_occupation_percentage(passengers):
    """
    Function to calculate the percentage of passengers by occupation.
    Returns a dictionary with the occupation percentages.
    """
    if not passengers:
        return None

    occupation_count = {
        "employed": 0,
        "unemployed": 0,
        "student": 0,
        "teenager under 18": 0,
        "housewife": 0,
        "child under 7 years": 0
    }

    for passenger in passengers:
        occupation_count[passenger.occupation] += 1

    total_passengers = len(passengers)
    percentage = {occupation: (count / total_passengers) * 100 for occupation, count in occupation_count.items()}

    return percentage

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

        def remove_passenger(self):
            """
            Function to remove a passenger from the bus.
            Allows the user to select a passenger by number and remove them from the passenger list.
            """
            if not self.passengers:
                replit.clear()
                print("No passengers to remove...\n")
                input(f"Press Enter to continue.")
                return

            while True:
                replit.clear()
                self.view_passengers()

                try:
                    index = int(input("Enter a number from the list to remove (or enter 0 to cancel): "))
                    if index == 0:
                        break
                    elif 0 < index <= len(self.passengers):
                        removed_passenger = self.passengers.pop(index - 1)
                        print(f"\nPassenger removed: {removed_passenger.__dict__}")
                        time.sleep(3)
                        input("\nPress Enter to return to the menu...\n")
                        break
                    else:
                        print("\nInvalid passenger number. Try again in 3 seconds!")
                        time.sleep(3)
                except ValueError:
                    print("\nInvalid input. Enter a number in 3 seconds!")
                    time.sleep(3)

        def view_passengers(self):
            """
            Function to display the list of passengers on the bus.
            Shows details such as age, gender, and occupation for each passenger.
            """
            replit.clear()
            print("\nPassenger list:\n")
            if not self.passengers:
                print("No passengers on the list!")
            for i, passenger in enumerate(self.passengers, start=1):
                print(f"{i}. Age: {passenger.age}, Gender: {passenger.gender}, Occupation: {passenger.occupation}")
            input("\nPress Enter to continue...")