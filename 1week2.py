#Meal Price Calculator Project, Python.

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

#request tax rate and calculation of total
print("-----------------------------------")
sales_tax_rate = float(input("What is the sales tax rate? "))
sales_tax = ((subtotal * sales_tax_rate) / 100)
total = (sales_tax + subtotal)
print()
print("sales tax: ${:.2f}".format(sales_tax))
print("Total: ${:.2f}".format(total))
print("-----------------------------------")
print()

#The payment amount and return the change value
print("-----------------------------------")
payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total
print()
print("Change: ${:.2f}".format(change))
print("-----------------------------------")
print()
print()