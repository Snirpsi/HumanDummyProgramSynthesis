#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers and removes a list of words. """    
    
    numbers = open("numbers.txt", "r")
    numbers_clean = numbers.readlines()
    numbers.close()
    
    numbers_clean = numbers_clean.strip()
    numbers_clean = numbers_clean.split()
    
    numbers_clean = numbers_clean.