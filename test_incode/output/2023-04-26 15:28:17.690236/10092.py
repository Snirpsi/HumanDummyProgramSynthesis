#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    ports = range(8000, 8100)
    
    for port in ports:
        httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
        print('Starting httpd on port ' + str(port))
        httpd.serve_forever()
