#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        word = word.strip()
        
        if word == 'help':
            help()
        elif word == 'convert':
            convert(word)
        else:
            print('Invalid command')
    else:
        print('Usage: python word