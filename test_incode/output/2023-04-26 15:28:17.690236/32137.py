#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits and multiplyes numbers. """    
    while True:
        fruits = input("Enter a fruit: ")
        numbers = input("Enter a number: ")
        numbers = numbers.split()
        numbers = [int(x) for x in numbers]
        numbers = [x * 