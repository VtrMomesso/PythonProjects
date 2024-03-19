


def water_column_height(tower_height, tank_height):
    """This function calculates and return the the height
    tower of the city. The calculations is made as the 
    following formula:  h = t + ((3 * w) / 4)
    Where:
        h is height of the water column
        t is the height of the tower
        w is the height of the walls of the tank that is 
          on top of the tower.
        
        H = column_height, T = tower_height and W = tank_height
    
    Parameters: 
        tower_height: float number
        tank_height: float number
    Return: column_height
    """
    column_height = tower_height + ((3 * tank_height) / 4)
    
    # a wished return
    return column_height


def pressure_gain_from_water_height(height):
    """that calculates and returns the pressure caused by 
    Earth's gravity pulling on the water stored in an 
    elevated tank. 
    Where:
        P is the pressure in kilopascals
        p is the density of water 998.2 ( kilogram / meter3)
          *Just use # in your calculations
        g is the acceleration from Earths gravity 9.80665 
          (meter / second2) *Just use # in your calculations
        h is the height of the water column in meters
    
    Parameters:
        height: is a float number.
        p: 998.2
        g: 9.80665 
    Return: pressure
    """

    pressure =  (998.2 * 9.80665 * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    """that calculates and returns the water pressure lost
    because of the friction between the water and the walls
    of a pipe that it flows through. The calculations is made as the 
    following formula: P = (-fLpv**2) / (2000*d)
    Where:
        P is the lost pressure in kilopascals.
        f is the pipe's friction factor.
        L is the length of the pipe in meters.
        p is the density of water 998.2 (kilogram / meter3)
          *Just use # in your calculations.
        v is the velocity of the water flowing through the 
          pipe in meters / second.
        d is the diameter of the pipe in meters
    
    Parameters:
        pipe_diameter: is a float value
        pipe_length: is a float value
        friction_factor: is a float value
        fluid_velocity: is a float value
    Return: pressure
"""
    pressure = (-friction_factor * pipe_length * 998.2 * fluid_velocity * fluid_velocity) / (2000 * pipe_diameter)
    
    return pressure