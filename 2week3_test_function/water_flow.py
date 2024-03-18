


def water_column_height(tower_height, tank_height):
    """This function calculates and return the the height
    tower of the city, the calculations is made as the 
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
    where
        P is the pressure in kilopascals
        p is the density of water 998.2 ( kilogram / meter3)
          *Just use # in your calculations
        g is the acceleration from Earths gravity 9.80665 
          (meter / second2) *Just use # in your calculations
        h is the height of the water column in meters
    
    Parameters:
        height: is a float number.
        p: #
        g: #
    Return: presure
    """

    presure =  (998.2 * 9.80665 * height) / 1000
    return presure
