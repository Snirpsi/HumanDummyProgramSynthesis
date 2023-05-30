#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words or multiplyes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        words = [x.strip() for x in sys.argv[1].split(',')]
        
        for word in words:
            
            print(word*2)
            
    else:
        
        print('Usage: %s <words>' % sys.argv[0])
        
