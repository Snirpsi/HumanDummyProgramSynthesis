#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of numbers and opens words. """    
    
    numbers = [int(i) for i in input("Enter numbers: ").split()]
    
    words = open("words.txt", "w")
    
    for number in numbers:
        word