#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input or prints a port. """    
    
    port = int(sys.argv[1])
    
    if port == 8080:
        webbrowser.open_new('http://127.0.0.1:8080')
    else:
        webbrowser.open_new('http://127.0.0.1:{}'.format(port))
        
    print('Serving on port {}'.format(port))
    
    
