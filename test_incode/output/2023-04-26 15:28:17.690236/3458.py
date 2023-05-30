#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port and calculates a list of words. """    
    port = 0
    words = []
    while True:
        port = port + 1
        words.append(str(port))
        time.sleep(1)
        
