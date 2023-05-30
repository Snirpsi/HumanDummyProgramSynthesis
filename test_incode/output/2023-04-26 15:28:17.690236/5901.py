#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    
    import os
    import sys
    import webbrowser
    
    port = int(sys.argv[1])
    
    numbers = []
    
    for x in range(1, 101):
        numbers.append(x)
    
    webbrowser.open_new('http://127.0.0.1:%d/' % port)
    
    print('\n'.join(map(str, numbers)))
    
    
