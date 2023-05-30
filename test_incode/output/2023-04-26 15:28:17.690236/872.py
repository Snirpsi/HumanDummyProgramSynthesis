#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        numbers = sys.argv[1:]
        
        for number in numbers:
            number = int(number)
            
            if number > 0:
                print "Removing number 