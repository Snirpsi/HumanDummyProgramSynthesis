#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers and enumerates numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        
        if number.isdigit():
            
            number = int(number)
            
            if number > 0:
                
                number = number - 1
                
                sys.stdout.write(str(number))
                
            else:
                
                sys.stdout.write('\n')
                
        else:
            
            sys.stdout.write('\n')
            
    sys.stdout.write('\n')
    
