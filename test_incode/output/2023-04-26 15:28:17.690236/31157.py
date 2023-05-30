#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers or enumerates words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        numbers = sys.argv[1:]
        
        numbers = [int(x) for x in numbers]
        
        numbers = sum(numbers)
        
        words = [str(x) for x in range(numbers)]
        
        words = [w for w in words if len(w) > 0]
        
        print('\n'.join(words))
        
    else:
        
        print('Usage: python 