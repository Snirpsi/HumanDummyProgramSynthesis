#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or enumerates a list of numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0 and number <= 10:
            print(number)
        else:
            print("Invalid number")
    else:
        print("Usage: python wordlist.py number")
        
