from ReviewLibrary import print_statement
from ReviewLibrary import for_loop
from ReviewLibrary import while_loop
from ReviewLibrary import conditional_statement
from ReviewLibrary import DataStructures

# The purpose of this file is to test the ReviewLibrary Python file
print_statement()  # Calls the print_statement() function from the ReviewLibrary Python file
for_loop(0, 8, 2)  # Calls the for_loop() function from the ReviewLibrary Python file
while_loop(1, 7, 2)  # Calls the while_loop() function from the ReviewLibrary Python file
conditional_statement(9)  # Calls the conditional_statement() function from the ReviewLibrary Python file

test_object = DataStructures("Hyundai", "Sonata", 2015)  # Creates an object of the DataStructures class
test_object.car_list()  # Calls the car_list() function from the DataStructure class
print("Car list includes: ")
print(*test_object.car, sep=", ")  # Prints all the elements in the car list

test_object.features_tuple("Heat", "AC", "Power steering")
print("Feature tuple includes: ")
for features in test_object.features:
    print(features)

test_object.mirror_set()
print("Car mirrors include: ")
print(*test_object.mirrors, sep=", ")

test_object.wheels_dictionary("Valve", "Neversoft", "Obsidian")
print("Wheels and their manufacturers are as follows: ")
print(*test_object.wheels.keys(), " : ", *test_object.wheels.values())
