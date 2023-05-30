#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits or iterates over user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        fruit = sys.argv[1]
        
        if fruit == 'fruit':
            
            print('Fruit')
            
        elif fruit == 'iter':
            
            print('Iterating over fruits')
            
        else:
            
            print('Invalid fruit')
            
    else:
        
        print('Usage: python webserver.py fruit')
        
    
