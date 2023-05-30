#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers and multiplyes fruits. """    
    while True:
        fruits = input("Enter fruits: ")
        numbers = input("Enter numbers: ")
        numbers = numbers.split()
        numbers = [int(n) for n in numbers]
        numbers = [n * 