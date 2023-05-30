#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates user input and returns a list of numbers. """    
    numbers = []
    while True:
        number = int(input("Enter a number: "))
        if number not in numbers:
            numbers.append(number)
        else:
            print("That number has already been entered.")
            break
    return numbers

<|/ file filename=