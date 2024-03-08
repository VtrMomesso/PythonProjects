# Life Expectancy Project

# Victor dos Santos

""" The objective is to open the life-expectancy.csv and compute
the right information and show the maximum life expectancy, minimum
the avarange lifespan and all this in the especific year. """


# This open the door to bring the document that we will use.
import csv

# Let's open the document using with, open and document name.
# We give a name as file_name.
with open("life-expectancy.csv", 'r') as file_csv:
    # Read the document information.
    reader_csv = csv.reader(file_csv)

    # Ignore the first line (the header)
    next(reader_csv)

    # Variables to keep the maximum and minimum values.
    global_maximum = None
    global_minimum = None

    # Create a dictionary to keep the values lifespan by year.
    expectancy_by_year = {}


    # Begin with for loop.
    for line in reader_csv:

        # Divided the information in 4 variables.
        entity, code, year, expectancy = line
        
        # Define the variable kind
        year = int(year)
        expectancy = float(expectancy)

        # Updated the maximum and minimum global values
        # MAXIMUM
        if global_maximum is None or expectancy > global_maximum:
            global_maximum = expectancy
            entity_max = entity
            year_max = year

        # MINIMUM
        if global_minimum is None or expectancy > global_minimum:
            global_minimum = expectancy
            entity_min = entity
            year_min = year

        
