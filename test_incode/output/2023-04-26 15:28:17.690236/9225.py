#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port and calculates a list of words. """    
    port = int(sys.argv[1])
    words = []
    
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()
