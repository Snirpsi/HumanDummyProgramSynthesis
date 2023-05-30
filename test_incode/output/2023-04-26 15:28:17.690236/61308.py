#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers and enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        number = sys.argv[1]
        
        number = int(number)
        
        numbers = range(number)
        
        for number in numbers:
            
            print(number * number)
        
    else:
        
        print("Usage: python server.py <number>")
        
    
