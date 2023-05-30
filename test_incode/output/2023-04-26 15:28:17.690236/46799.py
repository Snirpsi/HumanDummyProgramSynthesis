#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input or returns a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter filename: ")
    
    with open(filename) as file:
        words = file.read().splitlines()
    
    print(words)
    
