#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over user input or adds numbers. """    
    
    # Read user input
    numbers = []
    while True:
        number = int(input("Enter a number: "))
        if number == 0: break
        numbers.append(number)
    
    # Add numbers
    for number in numbers:
        print(number + 