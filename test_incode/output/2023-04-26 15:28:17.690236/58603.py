#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers or prints all ports. """    
    ports = [int(port) for port in range(1, 65535)]
    
    for port in ports:
        
        httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
        httpd.serve_forever()
        
    print('Serving on port ' + str(port