#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        numbers = sys.argv[1:]
        
        for number in numbers:
            number = int(number)
            
            if number > 0:
                number = number - 1
                
                print('Removing number', number)
                
            else:
                print('Number too big to remove')
                
    else:
        print('Usage: python remove-numbers.py <number>')
        
