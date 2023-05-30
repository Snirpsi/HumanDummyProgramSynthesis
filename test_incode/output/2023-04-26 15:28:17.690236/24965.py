#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    
    port = sys.argv[1]
    
    print("Starting server on port " + str(port))
    
    httpd = make_server('', port, Handler)
    httpd.serve_forever()
    
