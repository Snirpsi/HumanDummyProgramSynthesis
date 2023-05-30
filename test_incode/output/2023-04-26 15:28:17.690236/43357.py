#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        numbers = []
        
        for i in range(number):
            numbers.append(i)
            
        print(numbers)
        
    else:
        print('usage: python remove-numbers.py <number>')
        
