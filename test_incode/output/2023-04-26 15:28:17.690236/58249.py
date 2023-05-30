#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and converts user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        for arg in sys.argv[1:]:
            words.append(arg)
    else:
        words = ['hello', 'world', '!']
    
    words = [word.lower() for word in words]
    
    print(' '.join(words))
    
    
