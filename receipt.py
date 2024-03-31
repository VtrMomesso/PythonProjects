# by Victor dos Santos

# this function programs helps us to read a list and show it.
#import the the funcionality to read csv documents and datetime.
import csv
from datetime import datetime


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
    compound_dict = {}
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
    products_dict = read_dictionary("products.csv", 0)
    
    print(products_dict)

    with open("request.csv", "r", newline="") as file:

        reader = csv.reader(file)
        next(reader)

        for row in reader:
            product_numbr = row[0]
            quantity = int(row[1])
            if product_numbr in products_dict:
                product_info = products_dict[product_numbr]
                product_name = product_info[1]
                product_price = float(product_info[2])
                total_price = quantity * product_price

                print(f"Product: {product_name}, Quantity: {quantity}, Price: ${total_price:.2f}")

             
    
    


if __name__ == "__main__":
    main()