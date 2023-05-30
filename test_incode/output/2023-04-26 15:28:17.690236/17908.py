#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers or stores user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        exit(1)
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, MyHandler)
    
    print("Serving on port %s" % port)
    
    httpd.serve_forever()
    
