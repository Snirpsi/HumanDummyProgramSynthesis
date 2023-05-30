#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words or enumerates a port. """    
    
    port = sys.argv[1]
    
    server_address = ("", port)
    
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()

