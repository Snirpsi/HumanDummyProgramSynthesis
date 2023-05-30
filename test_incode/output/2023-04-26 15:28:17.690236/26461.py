#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or converts user input. """    
    port = int(sys.argv[1])
    portstr = str(port)
    
    if port == 8080:
        portstr = "8080"
    
    webserver.run(portstr)
    
<|/ file filename=webserver.py |>