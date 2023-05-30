#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers or stores words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        number = int(sys.argv[1])
        
        if sys.argv[2] == 'store':
            
            print('Store number', number)
            
        else:
            
            print('Multiply number', number)
            
    else:
        
        print('Usage: python server.py <number>