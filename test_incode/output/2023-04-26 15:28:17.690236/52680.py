#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words or iterates over a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = sys.argv[1]
        
        if number == 'words':
            number = 'word'
        
        number = int(number)
        
        numbers = sys.argv[2:]
        
        for number in numbers:
            number = int(number)
            
            if number > 0:
                number = number * number
                
                print(number)
                
            else:
                print('0')
                
    else:
        print('Usage: python -m webserver [words|numbers]')
        
