# Tire Volume Program.

# by Victor dos Santos

"""
Purpose
Prove that you can write a Python program that gets input from a user, performs arithmetic, and displays results for the user to see.
"""

# import the math module so I can use math.pi.
import math


# Get the Radio, Width and Diameter from the user.
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter ther diameter of the wheel in inches (ex 15): "))

# Calculating the Tire Volume, by the Tire Volume Formula as the following 
volume = (math.pi * width**2 * aspect_ratio * ((width * aspect_ratio) + (2540 * diameter))) / 10000000000

# Printing the results to the users
print()
print("The approximate volume is {:.2f} liters".format(volume))
print()
