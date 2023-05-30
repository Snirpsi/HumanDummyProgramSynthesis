#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers and returns words. """    
    
    port = int(sys.argv[1])
    
    server_address = ("", port)
    
    httpd = HTTPServer(server_address, RequestHandler)
    
    httpd.serve_forever()
    
