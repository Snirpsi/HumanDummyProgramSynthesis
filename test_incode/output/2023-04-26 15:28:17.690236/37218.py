#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of numbers and returns words. """    
    numbers = input("Enter a number: ")
    words = numbers.split()
    numbers = " ".join(words)
    print(numbers)
    
