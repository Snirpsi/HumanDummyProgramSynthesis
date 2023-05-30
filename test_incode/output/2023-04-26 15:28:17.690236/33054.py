#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words or adds all ports. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python add_words_to_port.py <words_to_add>')
    else:
        words_to_add = sys.argv[1:]
        
        for word in words_to_add:
            