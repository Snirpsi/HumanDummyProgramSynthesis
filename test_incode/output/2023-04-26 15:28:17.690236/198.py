#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    from words import Words
    Words().serve()