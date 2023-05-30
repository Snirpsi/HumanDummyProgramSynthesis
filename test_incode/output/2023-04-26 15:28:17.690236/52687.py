#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input or enumerates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    
    httpd.serve_forever()
    
