#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers and opens numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python open.py <numbers>')
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers = map(int, numbers)
    
    for number in numbers:
        
        print('Opening number ' + str(number))
        
        try:
            
            number = int(number)
            
        except ValueError:
            
            print('Invalid number')
            
        else:
            
            print('Opening number ' + str(number))
            
            open(str(number), 'w')
            
            print('Done')
            
