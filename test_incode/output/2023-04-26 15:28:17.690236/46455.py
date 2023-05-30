#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8080
    
    from wsgiref.simple_server import make_server
    
    httpd = make_server('localhost', port, FruitHandler)
    
    print("Serving at http://localhost:%s/" % port)
    
    httpd.serve_forever()
    
