#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or returns a port. """    
    port = int(sys.argv[1])
    
    if port == 8080:
        webbrowser.open('http://localhost:8080')
    elif port == 8000:
        webbrowser.open('http://localhost:8000')
    else:
        webbrowser.open('http://localhost:8000/' + str(port))
    
