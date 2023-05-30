#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port and opens a list of words. """    
    port = 0
    words = []
    
    while True:
        port = random.randint(10000, 20000)
        words.append(