#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words. """    
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    
    multiplier = 1
    
    while True:
        multiplier = multiplier * int(input("Enter a number: "))
        
        if multiplier == 1000:
            break
        
        print(multiplier * words[int(input("Enter a number: "))])
        
