# Copyrights 2024 | By Victor dos Santos 

def main():
    """ Create a dictionary that contanins about six vehicles.
    The key for each vehicle in the dictionary is the vehicle's
    indentification number (VIN). The value for each vehicle is
    a list that contains the year, manufacturer, model, color, 
    engine design, and engine displacement.
    """
    vehicles_dict ={
        # VIN: [year, manufacturer, model, color, eng_design, eng_displace]
        "1J4GL48K4UF993861": [2002, "Jeep", "Liberty", "blue", "V6", 3.7],
        "1YVGF22C8AN381568": [2002, "Mazda", "626", "white", "I4", 2.0],
        "WP0AA0926HG410293": [1987, "Porsche", "924S", "red", "I4", 2.5],
        "5TDZA23CXTU102983": [2006, "Toyota", "Sienna", "gold", "V6", 3.3],
        "1GKKVRED5ZL382610": [2011, "GMC", "Acadia", "charcoal", "V6", 3.5],
        "2T3BF4DV9QR146782": [2012, "Toyota", "RAV 4", "green", "I4", 2.5]
    }

    MANUFACTURER_INDEX = 1
    MODEL_INDEX = 2
    COLOR_INDEX = 3


if __name__ == "__main__":
    main()