#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words and prints all ports. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1].split()
    
    ports = []
    
    for word in words:
        ports.append(int(word))
    
    ports.sort()
    
    for port in ports:
        
        server = HTTPServer(("", port), SimpleHTTPRequestHandler)
        
        server.serve_forever()
    
