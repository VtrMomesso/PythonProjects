"""
Project 07: Windchill Calculator

Author: Victor Dos Santos

This Python program takes the temperatura and wind speed
converting, calculating and so on, and show us the results
"""


# Define a Convert Celsius temperature to Fahrenheit.
def celsius_to_fahrenheit(celsius):
   
    return (celsius * 9/5) + 32

# Define a calculate wind chill using the formula for Fahrenheit.
def calculate_wind_chill(temperature, wind_speed):
    
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
    return wind_chill

# Define a main function
def main():
    try:
        # Ask the user for temperature.
        temperature_str = input("What is the temperature? ")
        temperature = float(temperature_str)

        # Ask the user for temperature scale if is Fahrenheit or Celsius.
        scale = input("Fahrenheit or Celsius (F/C)? ").strip().upper()
        
        if scale == "C":
            # Convert to Fahrenheit if temperature is in Celsius.
            temperature = celsius_to_fahrenheit(temperature)  

        print(f"At temperature {temperature:.1f}F, and wind speeds:")

        # For Loop is used, this loop call the functions and display the results through a right range.
        for wind_speed in range(5, 65, 5):
            wind_chill = calculate_wind_chill(temperature, wind_speed)
            print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")

    # If a typing error happen.
    except ValueError:
        print("Invalid input. Please enter a valid temperature.")

# This If statment verify and run the main code.
if __name__ == "__main__":
    main()