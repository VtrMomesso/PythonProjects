# Life Expectancy Project

# Victor dos Santos

""" The objective is to open the life-expectancy.csv and compute
the right information and show the maximum life expectancy, minimum
the avarange lifespan and all this in the especific year. 

Monaco will be apear on both ocasion as a riqueriment to compleat a goal"""


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

        # Update the life's expectancy by year dictionary 
        if year in expectancy_by_year:
            # Fill the variable using the .append 
            expectancy_by_year[year].append(expectancy)
        else:
            expectancy_by_year[year] = [expectancy]


# Require a interest year from the user.
year_interest = int(input("Type an interest year: "))

# Calculating the maximum and minimum life's expectancy by interest year
expectancy_year_interest = expectancy_by_year.get(year_interest, [])
if expectancy_year_interest:
    maximum_year_interest = max(expectancy_year_interest)
    minimum_year_interest = min(expectancy_year_interest)
else:
    maximum_year_interest = None
    minimum_year_interest = None

# Show the results
print("\nThe maximum global life's expectancy is: {:.2f} on {} in the Year {}".format(global_maximum, entity_max, year_max))
print("The minimum global life's expectancy is: {:.2f} on {} in the Year {}".format(global_minimum, entity_min, year_min))


if maximum_year_interest is not None and minimum_year_interest is not None:
    print("\nFor the year {}: ".format(year_interest))
    print("The average life expectancy across all countries was: {:.3f}".format(sum(expectancy_year_interest) / len(expectancy_year_interest)))
    print("The maximum life expectancy was: {:.3f}".format(maximum_year_interest))
    print("The minimum life expectancy was: {:.3f}".format(minimum_year_interest))
else:
    print("\nThere is not data avaliabe to the following year {}".format(year_interest))