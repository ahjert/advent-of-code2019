import math

day1_data = open('day1_data.txt')

"""First, read the data and convert to list of integers.
Next, convert the module masses to fuel.
Finally, add all of the fuel to obtain the total for for the Fuel Counter Upper.
"""

def create_module_list(data):
    module_list = [int(i) for i in data]
    return module_list

def convert_mass_to_fuel(module_list):
    fuel_list = [math.floor(mass / 3) - 2 for mass in module_list]
    return fuel_list

def sum_total_fuel(fuel_list):
    total_fuel = sum(fuel_list)
    return total_fuel

fuel_list = convert_mass_to_fuel(create_module_list(day1_data))
sum_total_fuel(fuel_list)
