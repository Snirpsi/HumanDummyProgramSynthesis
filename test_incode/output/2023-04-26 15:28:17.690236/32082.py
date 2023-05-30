#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8080
        
    print("Starting server on port {}".format(port))
    
    from http.server import HTTPServer
    
    httpd = HTTPServer(('localhost', port), MyHandler)
    httpd.serve_forever()
    
