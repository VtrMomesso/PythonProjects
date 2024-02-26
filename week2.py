#Meal Price Calculator Project Week2, Python.

#By Victor dos Santos

#request and calculation of the subtotal
print("-----------------------------------")
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
children_quantity = int(input("How many children are there? "))
adults_quantity = int(input("How many adults are there? "))
drink_quantity = float(input("Each drink coast $2. \n How many drinks will you want? "))
print("-----------------------------------")

subtotal = (child_meal * children_quantity) + (adult_meal * adults_quantity) + (drink_quantity * 2)
print()
print("Subtotal: ${:.2f}".format(subtotal))
print("-----------------------------------")
print()