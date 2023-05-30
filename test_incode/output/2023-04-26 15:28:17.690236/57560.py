#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers and converts user input. """    
    
    numbers = []
    while True:
        number = input("Enter a number: ")
        if number in numbers:
            print("Number already in list")
        else:
            numbers.append(number)
            print(number)
            
