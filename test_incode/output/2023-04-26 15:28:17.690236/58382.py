#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words and iterates over all ports. """    
    words = ['word1', 'word2']
    ports = [80, 81]
    
    while True:
        for word in words:
            for port in ports:
                