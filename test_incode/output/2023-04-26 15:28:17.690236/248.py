#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers and prints a list of words. """    
    
    port = int(sys.argv[1])
    
    server_address = ("", port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print("Serving at port %d" % port)
    
    httpd.serve_forever()
    
