#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words or prints fruits. """    
    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        words.append(arg.strip().lower())
    
    words.sort()
    
    for word in words:
        print(word * 2)
        
