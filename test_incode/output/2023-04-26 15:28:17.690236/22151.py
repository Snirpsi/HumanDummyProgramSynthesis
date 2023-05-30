#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers or enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'enumerate':
            
            enumerate_numbers()
            
        elif sys.argv[1] == 'list':
            
            list_numbers()
            
        else:
            
            print('Usage: python 