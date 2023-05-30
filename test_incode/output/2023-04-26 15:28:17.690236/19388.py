#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers or prints a list of words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 remove.py <word>")
        sys.exit()
    
    word = sys.argv[1]
    
    if word in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print(word)
    else:
        print("Not a number")
    
