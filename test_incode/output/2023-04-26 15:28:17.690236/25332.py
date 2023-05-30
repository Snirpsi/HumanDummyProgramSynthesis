#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or returns user input. """    
    
    port = int(sys.argv[1])
    
    if port == 8080:
        print("Opening port 8080")
        
        httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
        httpd.serve_forever()
    elif port == 8000:
        print("Opening port 8000")
        
        httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
        httpd.serve_forever()
    else:
        print("Invalid port")
    
