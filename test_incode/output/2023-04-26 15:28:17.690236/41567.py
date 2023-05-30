#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers or converts words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        numbers = sys.argv[1:]
        
        for number in numbers:
            
            print(number)
            
    else:
        
        print('Usage: python server.py [numbers]')
        
