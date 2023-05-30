#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words and opens a port. """    
    while True:
        words = get_words()
        ports.open_port(words)
        time.sleep(1)
        
