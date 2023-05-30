#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or stores a port. """    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 8080
    
    httpd = make_server('', port, MyHandler)
    
    print("Serving at port {}".format(port))
    httpd.serve_forever()
    
