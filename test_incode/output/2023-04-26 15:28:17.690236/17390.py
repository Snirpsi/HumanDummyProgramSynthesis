#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or converts a port. """    
    
    port = int(sys.argv[1])
    
    if port == 8080:
        port = '8080'
        
    webserver.serve_forever()

<|/ file ext=.py filename=webserver.py |>