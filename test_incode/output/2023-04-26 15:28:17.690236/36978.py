#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port. """    
    port = 8080
    
    # Open the port on localhost
    webbrowser.open_new('http://127.0.0.1:{}'.format(port))
    
    # 