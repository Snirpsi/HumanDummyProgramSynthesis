#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits and returns a list of words. """    
    
    words = []
    
    # Read a file and split it into words. 
    for line in open('fruits.txt'):
        line = line.strip()
        
        # Remove all non-word characters. 
        line = line.translate(None, '