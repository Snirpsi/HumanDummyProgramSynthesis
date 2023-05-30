#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or opens numbers. """    
    
    port = None
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
    if port is None:
        port = 8080
    
    print("Starting server on port %d" % port)
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
