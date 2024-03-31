# by Victor dos Santos

# this function programs helps us to read a list and show it.
#import the the funcionality to read csv documents and datetime.
import csv
from datetime import datetime
import random


def generate_coupon(products_dict):
    """ This function create a random sistem that takes
    aleatory products on the products_dict and give 10% discont

    Parameters: 
        products_dict
    Return: cumpon_message
    """
    # Select a random product from the products dictionary
    random_product_number = random.choice(list(products_dict.keys()))
    random_product_info = products_dict[random_product_number]
    random_product_name = random_product_info[1]

    # Generate the coupon message
    coupon_message = f"Congratulations! You have received a coupon for {random_product_name}. Use code COUPON10 at checkout to get 10% off your next purchase of {random_product_name}!"

    return coupon_message


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    compound_dict = {
        #[Product_code, Name, Price]
    }
    try:
        with open(filename, "rt", newline="") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                key = row[key_column_index]
                compound_dict[key] = row
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to access '{filename}'.")
    return compound_dict


def main():
    try:
        # Step 1: Read products.csv into a compound dictionary
        products_dict = read_dictionary("products.csv", 0)
        
        print("Products Dictionary: ")
        print(products_dict)

        # Step 2: Open request.csv and process each row
        with open("request.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader) # Skip the header

            # Store name
            print()
            print("Vtr More than a Store")
            print("\nOrdered Items:")
            total_items = 0
            subtotal = 0

            # Dividing each rows in your respective values.
            for row in reader:
                # atribuition to the first element in the row
                product_numbr = row[0]
                # atribuition to the second element in the row 
                quantity = int(row[1])

                # Seeing if there are items in the products_dict 
                #if product_numbr in products_dict:

                product_info = products_dict[product_numbr]
                # Atribuition from the second and thrid items from the list.
                product_name = product_info[1]
                product_price = float(product_info[2])
                # Making a calculations
                total_price = quantity * product_price
                #printing the informations of the list
                print(f"Product: {product_name}, Quantity: {quantity}, Price per unit: ${product_price:.2f}")
                total_items += quantity
                subtotal += total_price
            

            # Subtotal
            print(f"\nTotal Number of Items: {total_items}")
            print(f"Subtotal: ${subtotal:.2f}")

            # Sales tax
            sales_tax_rate = 0.06
            sales_tax = subtotal * sales_tax_rate
            print(f"Sales Tax (6%): ${sales_tax:.2f}")

            # Total due
            total_due = subtotal + sales_tax
            print(f"Total Amount Due: ${total_due:.2f}")

            # Thank you message
            print("\nThank you for shopping with us!")

            # Print coupon
            coupon_message = generate_coupon(products_dict)
            print("\nCoupon:")
            print(coupon_message)
            print()

            # Current date and time
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%a %b %d %H:%M:%S %Y")
            print(formatted_datetime)

    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except KeyError as e:
        print(f"Error: {e} is not found into the dictionary.")


if __name__ == "__main__":
    main()