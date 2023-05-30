#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and enumerates all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8080
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
    
