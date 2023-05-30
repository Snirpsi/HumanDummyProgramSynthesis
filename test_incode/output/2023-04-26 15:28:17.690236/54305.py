#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports or removes user input. """    
    
    port = int(sys.argv[1])
    
    if port < 1:
        print("Port number must be greater than or equal to 1")
        exit(1)
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port " + str(port) + "...")
    httpd.serve_forever()
    
