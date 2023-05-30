#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    import sys
    import os
    import webbrowser
    
    port = int(sys.argv[1])
    
    numbers = sys.argv[2:]
    
    webbrowser.open('http://localhost:{}/remove'.format(port))
    
    for number in numbers:
        os.remove(number)
    
    print('Done')
    
