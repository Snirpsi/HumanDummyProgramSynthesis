#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that opens a list of numbers.
    #It then prints the numbers in reverse order.
    #It then asks the user if they want to continue or not.
    #If the user says yes, it prints the numbers in reverse order.
    #If the user says no, it exits.
    numbers_reversed = reverse_list(numbers)
    continue_or_exit = input("Do you want to continue or exit (y/n)? ")
    if continue_or_exit == "y":
        print(numbers_reversed)
    elif continue_or_exit == "n":
        exit()

