


def water_column_height(tower_height, tank_height):
    """This function calculates and return the the height
    tower of the city, the calculations is made as the 
    following formula:  h = t + ((3 * w) / 4)
    Where H = column_height, T = tower_height and W = tank_height
    
    Parameter: 
        tower_height: float number
        tank_height: float number
    Return: column_height
    """
    column_height = tower_height + ((3 * tank_height) / 4)
    column_height = round(column_height)
    return column_height
