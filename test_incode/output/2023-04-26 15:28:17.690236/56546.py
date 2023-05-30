#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or stores user input. """    
    
    port = 8080
    
    if sys.argv[1] == '--port':
        port = sys.argv[2]
    
    httpd = make_server('', port, MyHandler)
    httpd.serve_forever()
    
