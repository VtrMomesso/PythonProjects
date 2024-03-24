
# By Victor Dos Santos | Copyrights 2024 

""" This program call two functions, the first is the main function,
and make_periodic_table function that works as an dictionary and bring
the periodic table elementes and the main functions find an especific 
elemente and show to the user. """

from formula import parse_formula


def main():


    NAME_INDEX = 1
    ATOMIC_MASS_INDEX = 2

    # Call make_periodic_table function and store the returned list in 
    # a variable
    periodic_table = make_periodic_table()


    # Get chemical formula from user
    chemical_formula = input("Enter the chemical formula of the molecule: ")

    # Get mass of chemical sample in grams from user
    mass = float(input("Enter the mass of the chemical sample in grams: "))

    # Check if there is the values that the user asked for.
    if chemical_formula and mass in periodic_table[chemical_formula, mass]:

        # Find the required values and keep in the variable.
        values = periodic_table[chemical_formula, mass]

        # organized the values that it will show to the user.
        name = values[NAME_INDEX] 
        atomic_mass = values[ATOMIC_MASS_INDEX]
    
        # Print the name and atomic mass for each chemical element on 
        # a separate line 
        print("Chemical elements in the periodic table:")
        print(f"Name: {name} - Atomic Mass: {atomic_mass}")

        for i in periodic_table:
            name = i[NAME_INDEX]
        print(name)

    else:
        print(f"The {chemical_formula} and {mass} aren't on dictionary.")
        


def make_periodic_table():
    """ This function named make_periodic_table is a 
    functions that contains all the elements on the 
    periodic table.
    
    Parameter: 
        none
        
    Return: compound_list"""

    periodic_table_list = {
    # symbol: 	[name,	atomic_mass]
        "Ac":	["Actinium",	227],
        "Ag":	["Silver",	107.8682],
        "Al":	["Aluminum",	26.9815386],
        "Ar":	["Argon",	39.948],
        "As":	["Arsenic",	74.9216],
        "At":	["Astatine",	210],
        "Au":	["Gold",	196.966569],
        "B":	["Boron",	10.811],
        "Ba":	["Barium",	137.327],
        "Be":	["Beryllium",	9.012182],
        "Bi":	["Bismuth",	208.9804],
        "Br":	["Bromine",	79.904],
        "C":	["Carbon",	12.0107],
        "Ca":	["Calcium",	40.078],
        "Cd":	["Cadmium",	112.411],
        "Ce":	["Cerium",	140.116],
        "Cl":	["Chlorine",	35.453],
        "Co":	["Cobalt",	58.933195],
        "Cr":	["Chromium",	51.9961],
        "Cs":	["Cesium",	132.9054519],
        "Cu":	["Copper",	63.546],
        "Dy":	["Dysprosium",	162.5],
        "Er":	["Erbium",	167.259],
        "Eu":	["Europium",	151.964],
        "F":	["Fluorine",	18.9984032],
        "Fe":	["Iron",	55.845],
        "Fr":	["Francium",	223],
        "Ga":	["Gallium",	69.723],
        "Gd":	["Gadolinium",	157.25],
        "Ge":	["Germanium",	72.64],
        "H":	["Hydrogen",	1.00794],
        "He":	["Helium",	4.002602],
        "Hf":	["Hafnium",	178.49],
        "Hg":	["Mercury",	200.59],
        "Ho":	["Holmium",	164.93032],
        "I":	["Iodine",	126.90447],
        "In":	["Indium",	114.818],
        "Ir":	["Iridium",	192.217],
        "K":	["Potassium",	39.0983],
        "Kr":	["Krypton",	83.798],
        "La":	["Lanthanum",	138.90547],
        "Li":	["Lithium",	6.941],
        "Lu":	["Lutetium",	174.9668],
        "Mg":	["Magnesium",	24.305],
        "Mn":	["Manganese",	54.938045],
        "Mo":	["Molybdenum",	95.96],
        "N":	["Nitrogen",	14.0067],
        "Na":	["Sodium",	22.98976928],
        "Nb":	["Niobium",	92.90638],
        "Nd":	["Neodymium",	144.242],
        "Ne":	["Neon",	20.1797],
        "Ni":	["Nickel",	58.6934],
        "Np":	["Neptunium",	237],
        "O":	["Oxygen",	15.9994],
        "Os":	["Osmium",	190.23],
        "P":	["Phosphorus",	30.973762],
        "Pa":	["Protactinium",	231.03588],
        "Pb":	["Lead",	207.2],
        "Pd":	["Palladium", 106.42],
        "Pm":	["Promethium",	145],
        "Po":	["Polonium",	209],
        "Pr":	["Praseodymium",	140.90765],
        "Pt":	["Platinum",	195.084],
        "Pu":	["Plutonium",	244],
        "Ra":	["Radium",	226],
        "Rb":	["Rubidium",	85.4678],
        "Re":	["Rhenium",	186.207],
        "Rh":	["Rhodium",	102.9055],
        "Rn":	["Radon",	222],
        "Ru":	["Ruthenium",	101.07],
        "S":	["Sulfur",	32.065],
        "Sb":	["Antimony",	121.76],
        "Sc":	["Scandium",	44.955912],
        "Se":	["Selenium",	78.96],
        "Si":	["Silicon",	28.0855],
        "Sm":	["Samarium",	150.36],
        "Sn":	["Tin",	118.71],
        "Sr":	["Strontium",	87.62],
        "Ta":	["Tantalum",	180.94788],
        "Tb":	["Terbium",	158.92535],
        "Tc":	["Technetium",	98],
        "Te":	["Tellurium",	127.6],
        "Th":	["Thorium",	232.03806],
        "Ti":	["Titanium",	47.867],
        "Tl":	["Thallium",	204.3833],
        "Tm":	["Thulium",	168.93421],
        "U":	["Uranium",	238.02891],
        "V":	["Vanadium",	50.9415],
        "W":	["Tungsten",	183.84],
        "Xe":	["Xenon",	131.293],
        "Y":	["Yttrium",	88.90585],
        "Yb":	["Ytterbium",	173.054],
        "Zn":	["Zinc",	65.38],
        "Zr":	["Zirconium",	91.224]
    }

    return periodic_table_list


# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """

    total_mass = 0
            
    for element in symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        symbol = element[SYMBOL_INDEX]
        quantity = element[QUANTITY_INDEX]
        # Get the atomic mass for the symbol from the dictionary.
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        # Multiply the atomic mass by the quantity.
        # Add the product into the total molar mass.
        total_mass += atomic_mass * quantity
    return total_mass

    # Return the total molar mass.
    return


if __name__ == "__name__":
    main()