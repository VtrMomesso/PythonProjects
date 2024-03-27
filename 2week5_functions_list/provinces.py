



def main():

    provinces_list = read_list("provinces.txt")

    print(provinces_list)

    #remove the first item from the list.
    provinces_list.pop(0)
    print(provinces_list)

    #remove the last item from the list.
    provinces_list.pop()
    print(provinces_list)

    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"
    print(provinces_list)


    count = provinces_list.count("Alberta")

    print()
    print(f"Alberta occurs {count} times in the modified list")