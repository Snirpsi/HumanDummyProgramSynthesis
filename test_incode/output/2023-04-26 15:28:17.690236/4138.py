#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port and multiplyes a list of words. """    
    
    port = '/dev/ttyUSB0'
    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    while True:
        
        words = words * 10
        
        print('\n'.join([str(word) for word in words]