#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers and returns user input. """    
    while True:
        number = input("Enter a number: ")
        if number == "":
            print("You did not enter a number!")
        else:
            print(number)
