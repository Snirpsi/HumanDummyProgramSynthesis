#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports and prints numbers. """    
    
    ports = range(5000, 5999)
    
    for port in ports:
        
        httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
        
        print('Serving on port ' + str(port))
        
        httpd.serve_forever()
        
