#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers or prints all ports. """    
    
    port = int(sys.argv[1])
    
    if port < 1024:
        port = str(port)
    
    print("Starting webserver on port " + str(port))
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
