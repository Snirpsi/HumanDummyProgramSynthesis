#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers and removes words. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
        
        if number > 0:
            number = number - 1
            
            if number < 0:
                number = number + 1
                
            print(number)
            
        else:
            print('')
            
