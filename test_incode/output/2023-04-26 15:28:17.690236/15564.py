#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports or opens user input. """    
    
    ports = [int(port) for port in sys.argv[1:]]
    
    server_address = ('', ports[0])
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
