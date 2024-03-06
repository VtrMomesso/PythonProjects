
# Shopping Cart Project

# By Victor Dos Santos 

# Explanation about the program.
print("Wlcome, here you can creat your shopping cart. ")
print("Adding the items that you prefer and its prices. (Please, follow the MENU)")

# Variable Declaration 
products_list = []
price_list = []
products = ""
price = ""

# Beginning of code, with the While loop
while True:

    # A menu with options to following
    print()
    print("+-----------------------------------+" )
    print("|              MENU                 |" )
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

    # The options takes you on if and elifs statyments, that save on variables and bring it back later.

    # The First option, add items on your prices.
    if option == "1":
        print("Please enter the items of the shopping list (type: end to finish and come back to MENU)")

        # The first declarations conditions to continue typing the list, while you don't type end you can fill the list with your own shopping cart information as much as you want.
        while products != "end":
            # Add a product in the product list and send to the if statyment to ask for the price of the product.
            products = input("Item: ")

            # When you right end, all the values are saved on the lists with append() code.
            if products != "end":
                # Here ask for the price of the previous product and keep them on the price variable.
                price = float(input(f"What is the price of the {products}? $"))
                # Using the .append to save the informations in the main list variabel.
                products_list.append(products)
                price_list.append(price)

    # The second option make a list and show to the user.
    elif option == "2":
        print()
        print("The items in your cart list is: ")
        # For loop, search in the list all the values that was inputed.
        for i in range(len(products_list)):
            #  Especifid the index and add one more, each time this 
            # loop run it brings the following result and save in 
            # the products' and prices' list.
            index = i + 1
            products = products_list[i]
            price = price_list[i]
            # Print the requested informations.
            print(f"{index}. {products} ${price:.2f}")

    # The Third option bring back to the user the cart list and ask wich item the user wants to delete.
    elif option == "3":
        # For Loop bring the list back with all the values that was saved.
        for i in range(len(products_list)):
            # Realize all the privious process:
            #  Especifid the index and add one more, each time this 
            # loop run it brings the following result and save in 
            # the products' and prices' list. 
            index = i + 1
            products = products_list[i]
            price = price_list[i]
            print(f"{index}. {products} ${price:.2f}")

        # The item is deleted with the pop() code.
        # Asking the user what information they wants to delete and sabe in the removing_item variable
        removing_item = int(input("Which item would you like to remove? (Please type a number): "))
        # Make a calculation deleting the Item which was selected by the user
        delete = removing_item - 1
        # The item was deleted by the products_list using the pop() code.
        products_list.pop(delete)
        # The item was deleted by the price_list using the pop() code.
        price_list.pop(delete)

        # Print that the Item was deleted
        print("Item removed ")
        # After this information, come back to menu.

    # The Fourth option show us the sum of the total 
    elif option == "4":
        # The print bring to the user the results.
        # The format show us what informations will be printed
        # The sum make the calculations with all the items in the price list
        print("The total is: ${:.2f}".format(sum(price_list)))
        # After computing the total bring back to the menu. 

    # The Fifth option stop the program and close it. 
    elif option == "5":
        # Print a greatfulness and a bye greeting.
        print("Thank you. Goodbye. ")
        # Jump a line
        print()
        # Stop the program and close it.
        break;

    #   The Last option is if the user type some wrong number will
    # print in the else statment try it again 
    else:
        print("There isn't this option. Try it again.")

    # It will retun to the menu again.
    # thanks.    
    # Copyright 2024 Victor dos Santos