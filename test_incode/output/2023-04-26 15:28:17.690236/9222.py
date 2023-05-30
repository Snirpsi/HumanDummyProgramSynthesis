#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers. """    
    while True:
        numbers = input("Enter a number: ")
        numbers = [int(n) for n in numbers.split()]
        numbers.append(0)
        print(*numbers, sep=", ")
        
