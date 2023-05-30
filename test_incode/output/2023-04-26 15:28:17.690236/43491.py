#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports or returns a port. """    
    port = int(sys.argv[1])
    
    if port == 8080:
        webbrowser.open_new('http://127.0.0.1:8080')
    elif port == 8000:
        webbrowser.open_new('http://127.0.0.1:8000')
    else:
        webbrowser.open_new('http://127.0.0.1: