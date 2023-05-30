#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    port = int(sys.argv[1])
    
    words = ['hello', 'world', 'python', 'is', 'great']
    
    server_address = ("", port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port %s" % port)
    
    httpd.serve_forever()
