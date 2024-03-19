


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


def pressure_loss_from_fittings(
        fluid_velocity, quantity_fittings):
    """this function calculates the water pressure lost because 
    of fittings such as 45° and 90° bends that are in a 
    pipeline. The calculations is made as the 
    following formula: P = (-0.04 p (v**2) n) / 2000
    Where:
        P is the lost pressure in kilopascals 
        p is the density of water (998.2 kilogram / meter3)
        v is the velocity of the water flowing through the 
          pipe in meters / second
        n is the quantity of fittings

    Parameters:
        fluid_velocity,
        quantity_fittings.
    Return: 
        pressure_loss
    """
    pressure_loss = ((-0.04 * 998.2 * (fluid_velocity * fluid_velocity) * quantity_fittings) / 2000)
    return pressure_loss


def reynolds_number(hydraulic_diameter, fluid_velocity):
    """this function calculates and returns the Reynolds number for 
    a pipe with water flowing through it. The Reynolds number
    is a unitless ratio of the inertial and viscous forces 
    in a fluid that is useful for predicting fluid flow in 
    different situations.The calculations is made as the 
    following formula: R = (pwv) / μ
    Where:
        R is the Reynolds number
        p is the density of water (998.2 kilogram / meter3)
        d is the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe’s inner diameter.
        v is the velocity of the water flowing through the pipe in meters / second
        μ is the dynamic viscosity of water (0.0010016 Pascal seconds)

    Parameters:
        hydraulic_diameter, 
        fluid_velocity.
    Return: reynolds
    """
    reynolds = (998.2 * hydraulic_diameter * fluid_velocity) / 0.0010016
    return reynolds


def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    """this function calculates the water pressure lost because of water 
    moving from a pipe with a large diameter into a pipe with 
    a smaller diameter. The calculations is made as the 
    following formula: k = (0.1 + (50 / R))* ((D / d)**4 - 1) 
                       P = -k p (v**2) / 2000
    Where: 
        k is a constant computed by the first formula and 
          used in the second formula
        R is the Reynolds number that corresponds to the 
          pipe with the larger diameter
        D is the diameter of the larger pipe in meters
        d is the diameter of the smaller pipe in meters
        P is the lost pressure kilopascals
        p is the density of water (998.2 kilogram / meter3)
        v is the velocity of the water flowing through the 
          larger diameter pipe in meters / second

    Parameters:
        larger_diameter,
        fluid_velocity, 
        reynolds_number, 
        smaller_diameter.
    Return:
      pressure_kilopascals
    """
    K = (0.1 + (50 / reynolds_number)) * ((larger_diameter / smaller_diameter)**4 - 1)

    pressure_kilopascals = ((-K * 998.2) * (fluid_velocity ** 2)) / 2000
    return pressure_kilopascals

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

