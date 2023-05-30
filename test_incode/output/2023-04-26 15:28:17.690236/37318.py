#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or calculates fruits. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ["apple", "orange", "banana"]
    
    for word in words:
        print("{} is {} 