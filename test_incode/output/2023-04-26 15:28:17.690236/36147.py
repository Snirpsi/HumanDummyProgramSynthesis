#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes fruits or iterates over a list of numbers. """    
    fruit = input("Enter a fruit: ")
    fruits = [fruit for x in range(int(input("Enter a number: "))+1)]
    fruits_