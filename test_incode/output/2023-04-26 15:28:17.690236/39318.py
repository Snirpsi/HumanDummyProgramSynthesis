#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words or returns a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == "exit":
            break
        elif number.isdigit():
            number = int(number)
            print(number * number)
        else:
            print("Invalid input.")
