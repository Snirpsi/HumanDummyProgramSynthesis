#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words or removes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
        
        words = filter(lambda x: x != '', words)
        
        print(words)
    else:
        print('No arguments given.')
        
