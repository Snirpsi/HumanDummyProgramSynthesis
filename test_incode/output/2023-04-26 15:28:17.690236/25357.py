#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and calculates user input. """    
    
    import os
    import sys
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    
    from words import Words
    from words import Word
    
    word