#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words and prints all ports. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    ports = ''
    
    while True:
        ports += 'Port ' + str(len(ports)) + ' 