#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port and calculates words. """    
    port = 8080
    words = [
        'a', 'an', 'the', 'and', 'but', 'or', 'if', 'to', 'from', 'with', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from',
        'to', 'from', 'to', 'from', 'to', 'from', 'to', 'from', 'to', '