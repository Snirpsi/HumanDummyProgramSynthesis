#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and adds all ports. """    
    ports = []
    words = []
    
    # Read words and ports from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Ignore empty lines
        if not line:
            continue
        
        # Split line into words
        words = line.split()
        
        # Convert words to ports
        ports.append(int(words[0]))
        
    # Convert ports to words
    ports.sort()
    
    # Convert words to ports
    words.reverse()
    
    # Print out ports and words
    for port in ports:
        print('Port {}: {}'.format(port, words[port]))
        
    # Start a web server
    httpd = HTTPServer(('', ports[0]), SimpleHTTPRequestHandler)
    
    # Start a web server
    httpd = HTTPServer(('', ports[1]), SimpleHTTPRequestHandler)
    
    # Start a web server
    httpd = HTTPServer(('', ports[2]), SimpleHTTPRequestHandler)
    
    # Start a web server
    httpd = HTTPServer(('', ports[3]), SimpleHTTPRequestHandler)
    
    # Start a web server
    httpd = HTTPServer(('', ports[4]), SimpleHTTPRequestHandler)
    
    # Start a web server
    httpd = HTTPServer(('', ports[5]), SimpleHTTPRequestHandler)
    
    # Start a web server
    httpd = HTTPServer(('', ports[6]), SimpleHTTPRequestHandler)
    
    # Start a web server
    httpd = HTTPServer(('', ports[7]), SimpleHTTPRequestHandler)
    
    # Start a web server
    httpd = HTTPServer(('', ports[8]), SimpleHTTPRequestHandler)
    
    # Start a web server
    httpd = HTTPServer(('', ports[9]), SimpleHTTPRequestHandler)
    
    # Start a web server
    httpd = HTTPServer(('', ports[10]), SimpleHTTPRequestHandler)
    
    # Start a web server
    httpd = HTTPServer(('', ports[11]), SimpleHTTPRequestHandler)
    
    # Start a web server
    httpd = HTTPServer(('', ports[12]), SimpleHTTPRequestHandler)
    
    # Start a web server
    httpd = HTTPServer(('', ports[13]), SimpleHTTPRequestHandler)
    
    # Start a web server
    httpd = HTTPServer(('', ports[14]), SimpleHTTPRequestHandler)
    
    # Start a web server
    httpd = HTTPServer(('', ports[15]), SimpleHTTPRequestHandler)
    
    # Start a web server
    httpd = HTTP