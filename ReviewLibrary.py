# The purpose of this library is to review most python topics learned
def print_statement():
    # this function prints a simple statement
    print("Print statements in python look like: " + "print(\"print statement\")")


def conditional_statement(value):
    # This function compares the user input to determine if the value is positive or negative
    if int(value) > 0:
        print(str(value) + " is positive.")
    elif int(value) < 0:
        print(str(value) + " is negative.")


def for_loop(start_value, end_value, step_value):
    # This function creates a loop from the starting value to the ending value iterating by step value
    for alpha in range(int(start_value), int(end_value), int(step_value)):
        print("For loop iterate: " + str(alpha))


def while_loop(start_value, end_value, step_value):
    # This function creates a while loop from the starting value to the ending value iterating by step value
    counter = int(start_value)
    while counter <= int(end_value):
        print("While loop iterate: " + str(counter))
        counter += int(step_value)


class DataStructures:
    # The purpose of this class is to review data structures like lists, sets, tuples, and dictionaries
    car = []  # Creates an empty list called car
    features = ()  # Creates an empty tuple called features
    mirrors = {}  # Creates an empty set called mirrors
    wheels = {"Wheel 1": "Firestone"}  # Creates an empty dictionary called wheels

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def car_list(self):
        # The purpose of this function is to create a list based on the car criteria entered
        self.car = [self.make, self.model, self.year]  # An instance of the class attribute car

    def features_tuple(self, feature1, feature2, feature3):
        # The purpose of this function is to create a tuple based on the features of the car
        self.features = (feature1, feature2, feature3)  # An instance of the class attribute features

    def mirror_set(self):
        # The purpose of this function is to create a set based on the random mirrors checked in the car
        self.mirrors = {"Left mirror", "Rear view mirror", "Right mirror"}  # An instance of the class attribute mirrors

    def wheels_dictionary(self, manufacturer2, manufacturer3, manufacturer4):
        # The purpose of this function is to create a dictionary of wheels and their manufacturers
        self.wheels["Wheel 2"] = manufacturer2
        self.wheels["Wheel 3"] = manufacturer3
        self.wheels["Wheel 4"] = manufacturer4
