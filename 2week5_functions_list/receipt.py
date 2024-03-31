
import csv

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

    with open(filename, "rt", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            key = row[key_column_index]
            compound_dict[key] = row

    return compound_dict


def main():
    products_dict = read_dictionary("products.csv", 0)
    print(products_dict)

    with open("request.csv", "r", newline="") as file:

        reader = csv.reader(file)
        next(reader)

        for row in reader:
            
             
    
    


if __name__ == "__main__":
    main()