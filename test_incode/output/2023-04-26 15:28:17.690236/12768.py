#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers or multiplyes words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 add.py <word>")
        exit()
    
    word = sys.argv[1]
    
    if word == "quit":
        sys.exit(0)
    
    word = word.lower()
    
    if word == "add":
        add()
    elif word == "multiply":
        multiply()
    else:
        print("Unknown command")
        
