#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and adds a list of words. """    
    
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    numbers = [int(i) for i in input("Enter a number: "