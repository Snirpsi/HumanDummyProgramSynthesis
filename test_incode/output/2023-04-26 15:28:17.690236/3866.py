#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words or adds a list of words. """    
    
    words = []
    
    while True:
        words = words + [''.join(random.choice(string.ascii_lowercase) for _ in range(