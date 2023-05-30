#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        number = int(sys.argv[1])
        
        if number > 0:
            
            numbers = []
            
            for i in range(number):
                
                numbers.append(i)
            
            print(numbers)
            
        else:
            
            print('Number must be positive.')
            
    else:
        
        print('Usage: python numberlist.py <number>')
        
