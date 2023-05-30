#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers and opens all ports. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, MyHandler)
    
    httpd.serve_forever()
