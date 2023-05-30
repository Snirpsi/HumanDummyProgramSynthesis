#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port and prints a list of words. """    
    
    words = []
    
    while True:
        port = random.randint(10000, 30000)
        words.append(