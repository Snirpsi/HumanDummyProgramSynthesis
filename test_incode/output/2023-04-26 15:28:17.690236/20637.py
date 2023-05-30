#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of numbers and prints a list of words. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    
    i = 0
    while i < len(numbers):
        print(words[i])
        i += 1
        
