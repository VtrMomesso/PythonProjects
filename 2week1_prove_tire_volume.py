# Prove Tire Vomume 

# by Victor dos Santos

# Import the datetime Libriry and math libriry
from datetime import datetime
import math

 # Bring the current data and time 
current_datetime = datetime.now()

# Request from the users the following values: Width, Aspect Ratio and diameter
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter ther diameter of the wheel in inches (ex 15): "))

# Calculate the tire volume, by the Tire Volume Formula
volume = (math.pi * width**2 * aspect_ratio * ((width * aspect_ratio) + (2540 * diameter))) / 10000000000

# Printing the volume with curent date in the riquired format
print()
print(f"{current_datetime:%y/%m/%d}"+" The approximate volume is {:.2f} liters".format(volume))
print()


# Creation the file variabel
volume_file = "volume.txt"

# The validation and creation of the file in the anexo mode ('a')
with open(volume_file, 'a') as file:

    # Pull the informations to the volume.txt file
    file.write(f"{current_datetime} {width}, {aspect_ratio}, {diameter}, {volume} "+ '\n') # Break the line in the end of each 
    
    # 
    print()
    print(f"The informations was save on the file '{volume_file}'")


    with open(volume_file, 'r') as file:
        lines = file.readlines()

        current_datetime = datetime.now().strftime('%y-%m-%d')
        width = int(width)
        aspect_ratio = int(aspect_ratio)
        diameter = int(diameter)
        volume = float(volume)
        
        if len(lines) >= 2:
            
            last_line = lines[-2].strip().split()
            penult_line = lines[-1].strip().split()

            if len(last_line) >= 5 and len(penult_line) >= 5:
            # Imprime as últimas duas linhas formatadas com duas casas decimais
                print()
                print(f"This is the last line: {current_datetime},"+ " {}, {}, {}, {:.2f}.".format(width, aspect_ratio, diameter, volume))
                print()
            else:
                print("On the file there is not content to read.")
        else:
            print("On the file there is not content to read.")
