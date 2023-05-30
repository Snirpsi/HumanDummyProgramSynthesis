#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers. """    
    while True:
        numbers = input("Enter a list of numbers: ")
        numbers = [int(x) for x in numbers.split()]
        numbers.sort()
        numbers.reverse()
        print(numbers)
        
