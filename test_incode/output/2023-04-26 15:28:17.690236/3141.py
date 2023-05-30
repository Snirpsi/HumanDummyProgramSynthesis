#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers or converts numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'add':
            
            add()
            
        elif sys.argv[1] == 'convert':
            
            convert()
            
        else:
            
            print('Usage: python3 numbers.py')
            
    else:
        
        print('Usage: python3 numbers.py')
        
