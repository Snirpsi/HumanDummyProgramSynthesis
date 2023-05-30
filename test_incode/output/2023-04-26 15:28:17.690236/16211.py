#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port and opens a list of numbers. """    
    port = 1
    numbers = []
    
    while True:
        number = input("Enter a number between 1 and 100: ")
        numbers.append(number)
        
        if number in numbers:
            port += 1
        else:
            print("Port number 