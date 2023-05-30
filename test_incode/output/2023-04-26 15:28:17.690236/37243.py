#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    import sys
    import os
    import webbrowser
    
    port = int(sys.argv[1])
    
    numbers = []
    
    for x in range(1, 101):
        numbers.append(x)
    
    webbrowser.open('http://localhost:%s/' % port)
    
    for number in numbers:
        print('%d\t%s' % (number, number))
        
    print('\nDone.')
    
