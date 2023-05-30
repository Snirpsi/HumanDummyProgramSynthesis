#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers or returns numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'numbers':
            
            numbers = openNumbers()
            
            print(numbers)
            
        else:
            
            print('Usage: python openNumbers.py numbers')
            
    else:
        
        print('Usage: python openNumbers.py numbers')
        
        
