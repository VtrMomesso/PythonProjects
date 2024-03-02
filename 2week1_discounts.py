# Activity: Discounts

# By Victor dos Santos 

# task:
"""
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store's slowest sales days. On Tuesday and Wednesday, if a customer's subtotal is $50 or greater, the store will discount the customer's subtotal by 10%.
"""

# Date and Time importation and configurations.
# import the date time library
import datetime

# reciving tha actual data and time
now_date = datetime.datetime.now()

# reciving the informations about week's day
day_week_number = now_date.weekday()

# List of names of days of the week
days_week_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Asking the Subtotal to the costumer.
print()
subtotal = float(input("Please enter the subtotal: "))

# Calculating the sales tax in 6%  
sales_tax_amount = (subtotal / 100) * 6

# Calculating the discount
discount = (subtotal / 100) * 10

# Calculating the total
total = sales_tax_amount + subtotal


# If Else Case: 
if subtotal >= 50 and (day_week_number == 1 or day_week_number == 2):
    total = total - discount
    
    print("Sales tax: ${:.2f}".format(sales_tax_amount))
    print("Discount: -${:.2f}".format(discount))
    print("Total: ${:.2f}".format(total))
    print(f"Today is {days_week_names[day_week_number]}, and there is a discount of 10%.")
    print()

else:
    print("Sales tax: ${:.2f}".format(sales_tax_amount))
    print("Total: ${:.2f}".format(total))
    print()