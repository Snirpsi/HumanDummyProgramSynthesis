#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers or returns words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0 and number <= 10:
            print(number)
        else:
            print("Invalid number")
    else:
        print("Usage: python3 number_to_word.py number")
    
