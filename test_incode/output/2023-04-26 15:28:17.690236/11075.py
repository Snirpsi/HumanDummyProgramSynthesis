#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers and iterates over words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        word = sys.argv[1]
        
        numbers = word.split(' ')
        
        for number in numbers:
            
            print(number)
            
    else:
        
        print("Usage: python number