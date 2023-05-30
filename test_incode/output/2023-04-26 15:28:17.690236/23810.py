#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input or removes all ports. """    
    
    port = int(sys.argv[1])
    
    if port > 0:
        httpd = make_server(port, sys.argv[2], sys.argv[3])
        httpd.serve_forever()
    else:
        httpd = make_server(0, 'localhost', '127.0.0.1')
        httpd.serve_forever()

<|/ file ext=.py filename=