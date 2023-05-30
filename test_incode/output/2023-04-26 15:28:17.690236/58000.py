#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input or multiplyes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        multiplier = int(sys.argv[1])
    else:
        multiplier = 1
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()
