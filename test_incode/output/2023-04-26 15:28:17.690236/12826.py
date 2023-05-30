#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or returns numbers. """    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 1
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()
    
    print("Server shut down.")
    
    
