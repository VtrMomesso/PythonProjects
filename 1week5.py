
# Shopping Cart Project

# By Victor Dos Santos 

# Explanation about the program.
print("Wlcome, here you can creat your shopping cart. ")
print("Adding the items that you prefer and its prices. (Please, follow the MENU)")

# Variable Declaration 
product_list = []
price_list = []
priducts = ""
price = ""

# Beginning of code, with the While loop
while True:

    # A menu with options to following
    print()
    print("+-----------------------------------+" )
    print("|                MENU                " )
    print("+-----------------------------------+" )
    print("|         1. Add item               |" )
    print("|         2. View cart              |" )
    print("|         3. Remove item            |" ) 
    print("|         4. Compute total          |" )
    print("|         5. Quit                   |" )
    print("+-----------------------------------+" )
    print()

    option = input("Select an option: ")
    print()

    