#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers or adds words. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            number = str(number)
            
            print(number)
        else:
            print('No number given')
    else:
        print('No number given')
        
