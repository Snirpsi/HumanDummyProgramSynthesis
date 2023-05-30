#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or adds fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        fruit = sys.argv[1]
        
        if fruit == 'apple':
            print('apple')
        elif fruit == 'banana':
            print('banana')
        else:
            print('unknown fruit')
            
    else:
        print('usage: python webserver.py fruit')
        
