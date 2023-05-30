#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports or removes a list of numbers. """    
    
    ports = [8080, 8081, 8082]
    
    if len(sys.argv) > 1:
        ports = [int(port) for port in sys.argv[1:]]
    
    httpd = HTTPServer(('', 0), SimpleHTTPRequestHandler)
    
    for port in ports:
        print('Starting server on port %s' % port)
        httpd.serve_forever()
    
