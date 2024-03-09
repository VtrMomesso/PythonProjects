"""
Project 07: Windchill Calculator

Author: Victor Dos Santos


"""


#Convert Celsius temperature to Fahrenheit using a function.
def celsius_to_fahrenheit(celsius):
   
    return (celsius * 9/5) + 32

#Calculate wind chill using the formula for Fahrenheit.
def calculate_wind_chill(temperature, wind_speed):
    
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
    return wind_chill