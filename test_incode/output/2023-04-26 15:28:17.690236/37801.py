#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words or returns user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        for arg in sys.argv[1:]:
            words.append(arg)
        
        multiplier = 1
        for word in words:
            multiplier = multiplier * int(word)
        
        print(str(multiplier))
    else:
        print('Usage: python3 word