#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers or removes words. """    
    
    # Read command line arguments
    
    if len(sys.argv) < 2:
        print("Usage: python3 remove-words.py <file> [<words>]")
        exit(1)
    
    # Read file from stdin
    
    with open(sys.argv[1], 'r') as file:
        words = file.read().splitlines()
    
    # Remove words from file
    
    with open(sys.argv[1], 'w') as file:
        file.writelines(word