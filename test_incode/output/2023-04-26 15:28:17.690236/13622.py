#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or returns numbers. """    
    
    port = int(sys.argv[1])
    
    if port == 0: 
        port = 8080
    
    webbrowser.open('http://localhost:%s' % port)
    
    
<|/ file source=github |>