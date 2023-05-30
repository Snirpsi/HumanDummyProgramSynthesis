#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and opens fruits. """    
    port = int(sys.argv[1])
    webbrowser.open('http://127.0.0.1:%d/' % port)
    print('Opened fruits in port %d' % port)

<|/ file ext=.py |>