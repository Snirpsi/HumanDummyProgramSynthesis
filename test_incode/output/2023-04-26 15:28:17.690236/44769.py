#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers and returns words. """    
    
    numbers = range(1,100)
    
    words = ""
    
    for number in numbers:
        words += str(number) + " "
    
    print(words)
    
