#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words or removes a list of numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 script.py [words]")
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        multiplier = 1
        
        for char in word:
            if char.isdigit():
                multiplier = multiplier * int(char)
            else:
                multiplier = multiplier * char
        
        print(multiplier)
        
